import os
import shelve
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("LLM_API_KEY")
WORKSPACE_ID = os.getenv("LLM_WORKSPACE_ID")
THREAD_ID = os.getenv("LLM_THREAD_ID")
API_HOST = os.getenv("LLM_API_HOST")

ssl_verify = False

class AnythingLLMClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def isAuthenticate(self):
        """Check autentication is ok"""
        url = f'{self.base_url}/api/v1/auth'  # Replace with actual endpoint
        try:
            response = requests.get(url, headers=self.headers,verify=ssl_verify)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f'Error during authentication: {e}')
            return None

    def post_message(self, workspace_id, thread_id, message):
        """Post a message to a chat thread."""
        url = f'{self.base_url}/api/v1/workspace/{workspace_id}/thread/{thread_id}/chat'  # Adjust endpoint as necessary
        data = {
            'message': message,
            'mode' : 'chat',
            'userId' : 1
        }
        try:
            response = requests.post(url, json=data, headers=self.headers, verify=ssl_verify)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f'Error posting message: {e}')
            return None

class AnythingLLMService:
    def __init__(self, base_url, api_key, workspace_id, thread_id):
        self.client = AnythingLLMClient(base_url=base_url, api_key=api_key)
        self.workspace_id = workspace_id
        self.thread_id = thread_id

    def authenticate(self):
        """Check authentication status."""
        return self.client.isAuthenticate()

    # Note: In the current implementation, there's no equivalent for file uploading in AnythingLLMClient class

    # Use context manager to ensure the shelf file is closed properly
    def check_if_thread_exists(self, wa_id):
        with shelve.open("threads_db") as threads_shelf:
            return threads_shelf.get(wa_id, None)

    def store_thread(self, wa_id, thread_id):
        with shelve.open("threads_db", writeback=True) as threads_shelf:
            threads_shelf[wa_id] = thread_id

    def generate_response(self, message_body, wa_id, name):
        # Check if there is already a thread_id for the wa_id
        thread_id = self.check_if_thread_exists(wa_id)

        # If a thread doesn't exist, use the default thread_id from initialization
        if thread_id is None:
            print(f"Using existing thread for {name} with wa_id {wa_id}")
            thread_id = self.thread_id

        post_response = self.client.post_message(self.workspace_id, thread_id, message_body)

        if post_response:
            new_message = post_response['textResponse']  # Adjust this based on the actual response structure
            return new_message
        else:
            print('Failed to get a response')
            return None


## Create an instance of AnythingLLMService and check authentication
# service = AnythingLLMService(base_url=f'https://{API_HOST}', api_key=API_KEY, workspace_id=WORKSPACE_ID, thread_id=THREAD_ID)

# auth_response = service.authenticate()
# if auth_response:
#     print('Authenticated successfully:', auth_response)

#     message = "Bonjour petit monsieur ! Que sais-tu faire?"
#     wa_id = "user_whatsapp_id"
#     name = "User Name"

#     response = service.generate_response(message, wa_id, name)
#     print('Response:', response)
# else:
#     print('Authentication failed')

# client = AnythingLLMClient(base_url=f'https://{API_HOST}', api_key=API_KEY)

# # Authenticate first, if necessary
# auth_response = client.isAuthenticate()
# if auth_response:
#     print('Authenticated successfully:', auth_response)

#     post_response = client.post_message(WORKSPACE_ID, THREAD_ID, 'Hello, how are you?')
#     if post_response:
#         print('Message posted successfully:', post_response)
#     else:
#         print('Failed to post message')
# else:
#     print('Authentication failed')