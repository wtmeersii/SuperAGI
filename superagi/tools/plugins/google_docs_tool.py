from superagi.tools import Tool
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

class GoogleDocsPlugin(Tool):
    def __init__(self, credentials):
        super().__init__()
        creds = Credentials.from_service_account_info(credentials)
        self.service = build('docs', 'v1', credentials=creds)

    def read_document(self, document_id):
        # Code to read a Google Doc
        pass

    def write_document(self, document_id, content):
        # Code to write to a Google Doc
        pass

    def read_document(self, document_id):
        document = self.service.documents().get(documentId=document_id).execute()
    return document

    def write_document(self, document_id, content):
        requests = [
            {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': content
            }
        }
    ]
    result = self.service.documents().batchUpdate(
        documentId=document_id, body={'requests': requests}).execute()
    return result
