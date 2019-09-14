import json

class ETLClient:
    def run(self, service, max_requests):
        """
        Handle max_requests calls to the given DocumentService.
        RetryImmediatelyError should be silently ignored and should *not*
        count as a request.
        Return document list.
        Content truncated due to max data buffer of 50kb being reached. Try flushing buffer with less content.

        Please write a simple ETL client for an fake document service.

        Requirements
        1: run() must return a JSON string.
        See test_req_1

        2: run() must return a JSON string as a dictionary, containing:

        'doc-count': [integer] the number of documents received
        'error-count':[integer] the number of errors received
        'docs': [dictionary] keys are a document's ID string and values are arrays of words in the document
        See test_req_2
        3: all of run()'s output words must be lower case
        See test_req_3

        4: these words must not appear in the word array: and, or, not, but, to, in
        See test_req_4

        5: RetryImmediatelyError.
        The service's handle_request() may raise RetryImmediatelyError.
        Do not count the error against the number of requests to run.
        Re-try the operation (by calling the handle_request() again) until successful.
        Include the number of errors in the output as in described in 2 above.
        See test_req_5

        6: The service may ask you to 'update' docs. These requests will look like:

          {'operation': 'update',
            'document': {
              'id': [string] document id
              'data': [string] new document data
              }
          }
        Expect that the document ID will match an existing document previously sent by an 'add' operation.
        The document with the matching ID should have its data replaced with the data sent in the 'update' operation.
        See test_req_6

        7:
        The service may ask you to 'delete' docs. These requests will look like:

          {'operation': 'delete',
            'document-id': [string] document id
           }
        Expect that the document ID will match an existing document previously sent by an 'add' operation.
        Delete the document that matches that ID.
        See test_req_7
        """
        documents = []

        documents.append({
                            'doc-count': 0,
                            'error-count': 0,
                            'docs': {}
                            })

        for i in range(0, max_requests):

            while True:

                try:
                    event = service.handle_request()

                    if event['operation'] == 'add':
                        # 'add': service sends us:
                        # {'operation':'add','document':{'data':'<words>','id':'<doc-id>'}}
                        doc_id = event['document']['id']
                        doc_data = self.remove_words(event['document']['data'])

                        # adds new doc_id and data
                        documents[0]['docs'][doc_id] = doc_data

                        # counts number of documents
                        documents[0]['doc-count'] = documents[0].get('doc-count') + 1

                    if event['operation'] == 'update':
                        doc_id = event['document']['id']
                        doc_data = self.remove_words(event['document']['data'])

                        # updates doc data by on doc id
                        documents[0]['docs'][doc_id] = doc_data

                    if event['operation'] == 'delete':
                        # removes document
                        doc_id = event['document-id']
                        docs = documents[0]['docs']
                        for docid, data in docs.items():
                          if docid == doc_id:
                              del docs[docid]

                        # subtracts 1 from number of documents
                        documents[0]['doc-count'] = documents[0].get('doc-count') - 1

                except RetryImmediatelyError:
                    # counts number of retry errors
                    documents[0]['error-count'] = documents[0].get('error-count') + 1
                    continue

                break

        return json.dumps(documents[0])


    def remove_words(self, string):
        # sanitizes string data in documents

        remove_words = set(['and', 'or', 'not', 'but', 'to', 'in'])
        words = string.lower().split(' ')

        for word in words:
            if word in remove_words:
                words.remove(word)

        return words



class Test(unittest.TestCase):
    def test_req_1(self):
        self.assertIsInstance(ETLClient().run(DocumentService(2), 1), basestring)

    def test_req_2(self):
        r = ETLClient().run(DocumentService(2), 2)
        expect = [
            json.dumps({
                'doc-count': 2,
                'error-count': 0,
                'docs': {
                    'f01dba4999266bff87400756e8830528': "aliquid cum ut labore nesciunt Voluptatibus eius Fugiat Sunt not error Nulla vitae rerum".split(),
                    '87e8d5ee79eb735b2e4e4fb88a9438e9': "nihil natus Voluptatibus aperiam Quo".split()
                }
            }),
            json.dumps({
                'doc-count': 2,
                'error-count': 0,
                'docs': {
                'f01dba4999266bff87400756e8830528': "aliquid cum ut labore nesciunt voluptatibus eius fugiat sunt not error nulla vitae rerum".split(),
                '87e8d5ee79eb735b2e4e4fb88a9438e9': "nihil natus voluptatibus aperiam quo".split()
                }
            }),
            json.dumps({
                'doc-count': 2,
                'error-count': 0,
                'docs': {
                'f01dba4999266bff87400756e8830528': "aliquid cum ut labore nesciunt voluptatibus eius fugiat sunt error nulla vitae rerum".split(),
                '87e8d5ee79eb735b2e4e4fb88a9438e9': "nihil natus voluptatibus aperiam quo".split()
                }
            })
        ]
        self.assertIn(r,expect)

    def test_req_3(self):
        r = ETLClient().run(DocumentService(2), 2)
        expect = [
            json.dumps({
                'doc-count': 2,
                'error-count': 0,
                'docs': {
                    'f01dba4999266bff87400756e8830528': "aliquid cum ut labore nesciunt voluptatibus eius fugiat sunt not error nulla vitae rerum".split(),
                    '87e8d5ee79eb735b2e4e4fb88a9438e9': "nihil natus voluptatibus aperiam quo".split()
                }
            }),
            json.dumps({
                'doc-count': 2,
                'error-count': 0,
                'docs': {
                    'f01dba4999266bff87400756e8830528': "aliquid cum ut labore nesciunt voluptatibus eius fugiat sunt error nulla vitae rerum".split(),
                    '87e8d5ee79eb735b2e4e4fb88a9438e9': "nihil natus voluptatibus aperiam quo".split()
                }
            })
        ]
        self.assertIn(r,expect)

    def _ordered(self, obj):
        """
        sorts multi-level objects recursively
        """
        if isinstance(obj, dict):
            return sorted((k, self._ordered(v)) for k, v in obj.items())
        if isinstance(obj, list):
            return sorted(self._ordered(x) for x in obj)
        else:
            return obj

    def test_req_4(self):
        r = ETLClient().run(DocumentService(2), 2)
        expect = json.dumps({
            'doc-count': 2,
            'error-count': 0,
            'docs': {
                'f01dba4999266bff87400756e8830528': "aliquid cum ut labore nesciunt voluptatibus eius fugiat sunt error nulla vitae rerum".split(),
                '87e8d5ee79eb735b2e4e4fb88a9438e9': "nihil natus voluptatibus aperiam quo".split()
            }
        })
        self.assertIn(self._ordered(r),self._ordered(expect))

    def test_req_5(self):
        r = ETLClient().run(DocumentService(2), 3)
        expect = json.dumps({
            'doc-count': 3,
            'error-count': 1,
            'docs': {
                'f01dba4999266bff87400756e8830528': "aliquid cum ut labore nesciunt voluptatibus eius fugiat sunt error nulla vitae rerum".split(),
                '87e8d5ee79eb735b2e4e4fb88a9438e9': "nihil natus voluptatibus aperiam quo".split(),
                '43e18d33e6b052a1f0b04d22b60f2059': "non occaecati accusantium animi eius sit placeat fugit dolor voluptate iure a".split()
            }
        })
        self.assertIn(self._ordered(r),self._ordered(expect))

    def test_req_6(self):
        r = ETLClient().run(DocumentService(6), 3)
        expect = json.dumps({
            'doc-count': 2,
            'error-count': 1,
            'docs': {
                'd740a7c5c4cb68a38c4cad51cc713a4f': 'quia consectetur maiores mollitia'.split(),
                '9491e81a43723db0c05e94662f06b6f3': 'ut accusantium recusandae animi velit labore id iure voluptate vel enim quo consequatur saepe'.split()
            }
        })
        self.assertIn(self._ordered(r),self._ordered(expect))

    def test_req_7(self):
        r = ETLClient().run(DocumentService(6), 9)
        expect = json.dumps({
            'doc-count': 0,
            'error-count': 1,
            'docs': {
            }
        })
        self.assertIn(self._ordered(r),self._ordered(expect))
