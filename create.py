from __future__ import print_function
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from app.models import Appreq
import dateutil.parser as parser
try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'App'
def get_credentials(request):
    home_dir = os.path.expanduser('~')
    t = request.session['ID']
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, '%s' %t)
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:
            credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
    return credentials
def main(request):
        credentials = get_credentials(request)
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar' , 'v3' , http=http)
        t = request.session['ID']
        for x in t:
         evnt = Appreq.objects.filter(ID__in=x, value='1').values_list('title')
         title = evnt[0]
         evnt = Appreq.objects.filter(ID__in=x, value='1').values_list('purpose')
         description = evnt[0]
         evnt = Appreq.objects.filter(ID__in=x, value='1').values_list('mail')
         attendee = evnt[0]
         evnt = Appreq.objects.filter(ID__in=x, value='1').values_list('start_date')
         start=evnt[0]
         text = '%s' %start
         start = text
         start = (parser.parse(text))
         start = start.isoformat()
         evnt = Appreq.objects.filter(ID__in=x, value='1').values_list('end_date')
         end=evnt[0]
         text = '%s' %end
         end = text
         end = (parser.parse(text))
         end = end.isoformat()
         evnt = Appreq.objects.filter(ID__in=x, value='1').values_list('mail')
         attendee = evnt[0]
         EVENT= {
                'summary' : '%s' %title,
                'description': '%s' %description,
                'start': {
                          'dateTime': start,
                          'timezone': 'Asia/Kolkata',
                          },
                'end':   {
                          'dateTime': end,
                          'timezone': 'Asia/Kolkata',
                          },
                'attendees': {
                                  'email': '%s' %attendee,
                                  },
                'reminders': {
                               'useDefault': False,
                               'overrides': [
                                              {'method': 'email', 'minutes': 24 * 60},
                                              {'method': 'popup', 'minutes': 10},
                                              ],
                                              },
           }
         event = service.events().insert(calendarId='primary',sendNotifications=True,body=EVENT).execute()
         print ('Event created: %s' % (event.get('htmlLink')))
         event_id = event.get('id')
         Appreq.objects.filter(ID__in=x,value='1').update(event_id=event_id)
if __name__ == '__main__' :
        main()
