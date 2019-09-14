import sys
import csv
import re


class FindMatches(object):
    """ Takes a .csv input file and a matching type and returns a copy of the original csv with the unique identifier of the person each row represents prepended to the row.

    Matching types:
    > email
    > phone
    > email_phone
    """

    def __init__(self, input_file, matching_type):
        """ Opens the csv file and declares the phone and email columns. """

        # Check if matching_type input is valid
        self.matching_type = matching_type.lower()
        if self.matching_type not in ['email', 'phone', 'email_phone']:
            print "Please use a valid matching type: 'email', 'phone', or 'email_phone'."

        # Initialize variables for later assignment
        self.input_file = input_file
        self.rownum = 0
        self.header = None
        self.email_col_2 = None
        self.email_col = None
        self.phone_col_2 = None
        self.phone_col = None

        # Keep track of entry duplicates/key assignments via ids dictionary
        self.ids = {}
        self.id = 1

        # Open the file with a csv reader
        csv_file_in = open(self.input_file, 'rU')
        reader = csv.reader(csv_file_in)

        # Declare the header for the file
        for row in reader:
            if self.rownum == 0:
                self.header = row
                self.rownum += 1
                break

        # Get the column number(s) for email
        for col in range(len(self.header)):
            if 'email2' in self.header[col].lower():
                self.email_col_2 = col
            if 'email1' in self.header[col].lower() or 'email' == self.header[col].lower():
                self.email_col = col

        # Get the column number(s) for phone
        for col in range(len(self.header)):
            if 'phone2' in self.header[col].lower():
                self.phone_col_2 = col
            if 'phone1' in self.header[col].lower() or 'phone' == self.header[col].lower():
                self.phone_col = col

        # Write to csv after all ids are assigned
        self.write_csv(reader, self.header)


    def email_match(self, row, min_id):
        """ Creates email tuples and insert unique tuples into the ids dictionary. """

        row_id = None

        # Assigns the id value to min_id if it exists, otherwise assigns it the next id value available
        if min_id:
            iden = min_id
        else:
            iden = self.id

        # Checks if a second email column exists
        if self.email_col_2:
            # Checks if value exists in second email column/row, and assigns it as the key
            if row[self.email_col_2]:
                email2 = row[self.email_col_2]
                self.add_key_to_dict(email2, iden)

                # If key exists in dictionary, assign it the row_id
                if self.ids.get(email2):
                    row_id = self.ids.get(email2)

        # Checks if value exists in first email column/row, and assigns it as the key
        if row[self.email_col]:
            email1 = row[self.email_col]
            # Sets the row_id to the minimum common value if it exists, otherwise sets it to the next available identifier value
            self.add_key_to_dict(email1, iden)
            row_id = self.ids.get(email1, self.id)

        # If no value in the field, sets the row_id to the next available identifier value
        if row_id is None:
            row_id = self.id

        return row_id


    def format_phone(self, row, column):
            """ Removes formatting of phone numbers for direct comparison. """

            format_phone_col = re.sub('\D+','',row[column])

            if len(format_phone_col) > 10:
                format_phone_col[1:]

            return format_phone_col


    def phone_match(self, row, min_id):
        """ Creates phone tuples and insert unique tuples into the ids dictionary. """

        row_id = None

        # Assigns the id value to min_id if it exists, otherwise assigns it the next id value available
        if min_id:
            iden = min_id
        else:
            iden = self.id

        # Checks if a second phone column exists
        if self.phone_col_2:
            # Checks if value exists in second phone column/row, and assigns it as the key
            if row[self.phone_col_2]:
                ids_key = self.format_phone(row, self.phone_col_2)
                self.add_key_to_dict(ids_key, iden)

                # If key exists in dictionary, assign it the row_id
                if self.ids.get(ids_key):
                    row_id = self.ids.get(ids_key)

        if row[self.phone_col]:
            ids_key = self.format_phone(row, self.phone_col)
            # Sets the row_id to the minimum common value if it exists, otherwise sets it to the next available identifier value
            self.add_key_to_dict(ids_key, iden)
            row_id = self.ids.get(ids_key, self.id)

        # If no value in the field, sets the row_id to the next available identifier value
        if row_id is None:
            row_id = self.id

        return row_id


    def add_key_to_dict(self, ids_key, iden):
        """ Places keys into a dictionary. If the key exists the key-value pair does not change. Otherwise, place it in the dictionary and assign it a new id. """

        self.ids[ids_key] = self.ids.get(ids_key, iden)


    def write_csv(self, reader, header, row_is_header=True):
        """ Using a csv writer, creates a copy of the file with unique ids prepended to each row. """

        csv_file_out = open('output_file.csv', 'w')
        writer = csv.writer(csv_file_out)

        while row_is_header:
            # Add 'id' column to header
            header = ['id'] + self.header

            # Write header row to new file
            writer.writerow(header)

            row_is_header = False

        # Runs matching type tests based on match type given
        for row in reader:
            row_id = None
            email_row_id = None
            phone_row_id = None

            # If the matching type is 'email'
            if self.matching_type == 'email':
                email2 = None
                email1 = None
                min_id = None

                # Check if email columns exist
                if self.email_col_2:
                    email2 = row[self.email_col_2]
                if self.email_col:
                    email1 = row[self.email_col]

                # Check if either email is in ids dictionary, get the value
                if email2 in self.ids or email1 in self.ids:
                    email2_exists = self.ids.get(email2)
                    email_exists = self.ids.get(email1)

                    # If multiple values exist, find the lowest and set that to min_id (row_id)
                    id_values = [email2_exists, email_exists]
                    min_id = min(iden for iden in id_values if iden is not None)

                # See if a second email column exists
                row_id = self.email_match(row, min_id)



            # If the matching type is 'phone'
            elif self.matching_type == 'phone':

                phone2 = None
                phone1 = None
                min_id = None

                # Check if phone columns exist
                if self.phone_col_2:
                    phone2 = self.format_phone(row, self.phone_col_2)
                if self.phone_col:
                    phone1 = self.format_phone(row, self.phone_col)

                # Check if either email is in ids dictionary, get the value
                if phone2 in self.ids or phone1 in self.ids:
                    phone2_exists = self.ids.get(phone2)
                    phone_exists = self.ids.get(phone1)

                    # If multiple values exist, find the lowest and set that to min_id (row_id)
                    id_values = [phone2_exists, phone_exists]
                    min_id = min(iden for iden in id_values if iden is not None)

                # See if a second phone column exists
                row_id = self.phone_match(row, min_id)


            # If the matching type is email OR phone
            elif self.matching_type == 'email_phone':

                email2 = None
                email1 = None
                phone2 = None
                phone1 = None
                min_id = None

                # Check if email and phone columns exist
                if self.email_col_2:
                    email2 = row[self.email_col_2]
                if self.email_col:
                    email1 = row[self.email_col]
                if self.phone_col_2:
                    phone2 = self.format_phone(row, self.phone_col_2)
                if self.phone_col:
                    phone1 = self.format_phone(row, self.phone_col)

                # Check if either email or phone is in ids dictionary, get the value
                if email2 in self.ids or email1 in self.ids or phone2 in self.ids or phone1 in self.ids:
                    email2_exists = self.ids.get(email2)
                    email_exists = self.ids.get(email1)
                    phone2_exists = self.ids.get(phone2)
                    phone_exists = self.ids.get(phone1)

                    # If multiple values exist, find the lowest and set that to min_id (row_id)
                    id_values = [email2_exists, email_exists, phone2_exists, phone_exists]
                    min_id = min(iden for iden in id_values if iden is not None)
                    row_id = min_id

                email_row_id = self.email_match(row, min_id)
                phone_row_id = self.phone_match(row, min_id)

                if email_row_id < phone_row_id:
                    row_id = email_row_id
                else:
                    row_id = phone_row_id

            # Writes a new row with the id appended
            new_row = [row_id] + row
            writer.writerow(new_row)

            # Increments id in ids dictionary for unique row ids
            self.id += 1



FindMatches(input_file=sys.argv[1], matching_type=sys.argv[2])


