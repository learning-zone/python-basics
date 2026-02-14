# Import the tkinter library for creating GUI applications
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Calculator")          # Set the window title
root.geometry("300x400")           # Set window size (width x height)

# Create an Entry widget to display numbers and results
entry = tk.Entry(
    root,
    font=("Arial", 20),             # Font style and size
    borderwidth=5,                  # Thickness of border
    relief="ridge",                 # Border style
    justify="right"                 # Align text to the right
)
entry.pack(fill="both", padx=10, pady=10)

# Function to insert numbers/operators when a button is clicked
def click(value):
    entry.insert(tk.END, value)     # Insert value at the end of the entry box

# Function to clear the display
def clear():
    entry.delete(0, tk.END)         # Delete everything from entry box

# Function to evaluate the expression
def calculate():
    try:
        # Evaluate the mathematical expression entered by the user
        result = eval(entry.get())
        entry.delete(0, tk.END)     # Clear entry box
        entry.insert(tk.END, result)  # Display result
    except:
        # If any error occurs (invalid expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# List of calculator buttons in order
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create a frame to hold all the buttons
frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

# Create buttons dynamically using a loop
for btn in buttons:
    if btn == "=":
        # '=' button performs calculation
        tk.Button(
            frame,
            text=btn,
            width=5,
            height=2,
            command=calculate
        ).grid(row=row, column=col)
    else:
        # Other buttons insert numbers/operators
        tk.Button(
            frame,
            text=btn,
            width=5,
            height=2,
            command=lambda b=btn: click(b)
        ).grid(row=row, column=col)

    col += 1
    if col > 3:                     # Move to next row after 4 buttons
        col = 0
        row += 1

# Clear button placed below the calculator buttons
tk.Button(
    root,
    text="Clear",
    width=20,
    height=2,
    command=clear
).pack(pady=10)

# Start the GUI event loop
root.mainloop()
