from __future__ import print_function
import httplib2
import os
import malespeaker

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def mails():
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    i=0
    result = ""
    malespeaker.speak("here are some of your mails:")
    results = service.users().labels().list(userId='me').execute()
    threads = service.users().messages().list(userId='me',q='label:promotions').execute().get('messages', [])
    for thread in threads :
        tdata = service.users().threads().get(userId='me', id=thread['id']).execute()
        nmsgs = len(tdata['messages'])
        f=0
        msg = tdata['messages'][0]['payload']
        subject = ''
        for header in msg['headers']:
            if header['name'] == 'From':
                sender = header['value']
                result=""
                result += "from:"+sender+"\n"
                print('from:',sender)
                f=1
            if header['name'] == 'Subject':
                subject = header['value']
                break
        if f==1 and subject:  # skip if no Subject line
            print('- %s (%d msgs)' % (subject, nmsgs))
            print()
            result += subject+"\n\n"
            #print(result)
            malespeaker.speak(result)
            f=0
        i+=1
        if i == 5:
            break

    return result



#    labels = results.get('labels', [])
#    if not labels:
#        print('No labels found.')
#    else:
#      print('Labels:')
#      for label in labels:
#        print(label['name'])


if __name__ == '__main__':
    mails()
