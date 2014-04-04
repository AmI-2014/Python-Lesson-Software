'''
Created on Mar 18, 2014

@author: Dario Bonino <dario.bonino@polito.it>

Copyright (c) 2014 Dario Bonino
 
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
 
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
'''
import imaplib, email, tts, time


def check_mail(user, pwd):

    '''
    Checks a gmail mailbox for new messages, and if any unread mail is found 
    provides a vocal rendering of the mail sender and subject
    '''
    
    # define the mail server (IMAP) in our case
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    
    # set the login parameters
    mail.login(user, pwd)
        
    # select the inbox
    mail.select('inbox')
    
    # Search for all new mail
    status, email_ids = mail.search(None, '(UNSEEN)')

    # get the e-mail ids
    if(len(email_ids[0].strip()) > 0):
        ids = email_ids[0].split(" ")

        # if there are unseen e-mails
        unreadcount = len(ids)
        if(unreadcount > 0):
            if(unreadcount > 1):
                tts.say("There are %d new messages" % (len(ids)))
            else:
                tts.say("There is one new message")
            
            # iterate over unread messages
            for i in range(0, unreadcount):
            
                # message number
                tts.say("Message %d:" % (i + 1))
                
                # get the full email contents
                status, data = mail.fetch(ids[i], "(RFC822)")
            
                # get the raw mail message
                raw_email = data[0][1]
                            
                # parse the mail message
                msg = email.message_from_string(raw_email)
                
                # warn about the message
                tts.say("You've got a new message from ")
                
                # render sender names
                for sender in msg.get_all('from', []):
                    tts.say(sender)
                
                # render subject
                tts.say("with subject")
                tts.say(msg.get('Subject', ''))

    mail.logout()

if __name__ == "__main__":
    while(True):
        # check for any new mail
        check_mail('domoticdog@gmail.com', ' uxrqsyiqiwewbont ')
        
        # wait 10s before next check
        time.sleep(5)
