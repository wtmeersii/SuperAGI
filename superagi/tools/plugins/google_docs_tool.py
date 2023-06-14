from superagi.tools import Tool
from googleapiclient import discovery
from google.oauth2 import service_account

class GoogleDocsTool(Tool):
    def __init__(self, credentials):
        super().__init__()
        self.credentials = service_account.Credentials.from_service_account_info(credentials)
        self.service = discovery.build('docs', 'v1', credentials=self.credentials)

        class GoogleDocsTool(Tool):
    # ...

    def run(self, title):
        document = self.service.documents().create().execute()
        requests = [
            {
                'insertText': {
                    'location': {
                        'index': 1,
                    },
                    'text': title
                }
            }
        ]
        result = self.service.documents().batchUpdate(
            documentId=document['documentId'], body={'requests': requests}).execute()
        return result
