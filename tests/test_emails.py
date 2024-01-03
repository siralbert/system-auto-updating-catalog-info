#!/usr/bin/env python3

import unittest
from ../emails import generate
from ../emails import send

class TestEmails(unittest.TestCase):
    def test_basic(self):
        testcase = { 'From' : 'automation@example.com',
                     'To' : 'username@example.com',
                     'Subject' : 'Upload Completed - Online Fruit Store',
                     'Body' : 'All fruits were uploaded to our website successfully.  A detailed list is attached to this email',
                     'Attachment' : 'processed.pdf'

        }
        expected = { 'From' : 'automation@example.com',
                     'To' : 'username@example.com',
                     'Subject' : 'Upload Completed - Online Fruit Store',
                     'Body' : 'All fruits were uploaded to our website successfully.  A detailed list is attached to this email',
                     'Attachment' : 'processed.pdf'
        }
        result = generate(testcase['From'],testcase['To'], testcase['Subject'], testcase['Body'],testcase['Attachment'])

        self.assertEqual(testcase['From'],expected['From'])
        self.assertEqual(testcase['To'],expected['To'])
        self.assertEqual(testcase['Subject'],expected['Subject'])
        #Will this work
        print(str(result.get_body()))
        self.assertEqual(testcase['Body'],str(result.get_body()))
        #Will this work
        self.assertIsNotNone(result.get(attachment))

unittest.main()

'''
def generate(sender, recipient, subject, body, attachment_path):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  # Process the attachment and add it to the email
  attachment_filename = os.path.basename(attachment_path)
  mime_type, _ = mimetypes.guess_type(attachment_path)
  mime_type, mime_subtype = mime_type.split('/', 1)

  with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                          maintype=mime_type,
                          subtype=mime_subtype,
                          filename=attachment_filename)

  return message


def send(message):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()
'''
