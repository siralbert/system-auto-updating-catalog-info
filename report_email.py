#!/usr/bin/env python3
 
import reports
import emails
import os
from datetime import date
 
 

# process_data function which opens list of descriptions and processes them to generate a report to send to the supplier
def process_data(path='supplier-data/descriptions'):
    report = []
    text_data = []
    # remove ending '/' if included in path
    if path.endswith('/'):
        path = path[:-1]
    list_text_files = [file for file in os.listdir(path) if '.txt' in file]
    for text_file in list_text_files:
      with open(os.path.join(path + '/' + text_file), 'r') as f:
        text_data.append([line.strip() for line in f.readlines()])
    for item in text_data:
      report.append("name: {}<br/>weight: {}\n".format(item[0], item[1]))
    return report
 
if __name__ == "__main__":
 
  summary = process_data()  # use default path='supplier-data/descriptions'

# Generate the PDF report
  paragraph = "<br/><br/>".join(summary) 
  title = "Processed Update on {}\n".format(date.today().strftime("%B %d, %Y"))
  attachment = "/tmp/processed.pdf" 
  reports.generate_report(attachment, title, paragraph)
 
# Send the email
  subject = "Upload Completed - Online Fruit Store"
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate_email(sender, receiver, subject, body, attachment)
  try:
    emails.send_email(message)
  except ConnectionRefusedError as e:
      print(f"\n {e}: Is the local SMTP server running and accepting requests on an open port (ie: port 25)?\n")
