#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

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

# def generate_email(sender, recipient, attachment=False):
#     message = EmailMessage()
#     message['From'] = sender
#     message['To'] = recipient
#     message['Subject'] = "Upload Completed - Online Fruit Store"
#     message.set_content = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

#     if attachment:
#         attachment_filename = os.path.basename(attachment)
#         mime_type, _ = mimetypes.guess_type(attachment)
#         mime_type, mime_subtype = mime_type.split('/', 1)

#         with open(attachment, 'rb') as ap:
#             message.add_attachment(ap.read(),
#                                     maintype=mime_type,
#                                     subtype=mime_subtype,
#                                     filename=attachment_filename)
#     return message

def send_email(message):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()


# def send_email(message, sender, recipient, smtp_server, smtp_port, sender_password=False):
#     mail_server = smtplib.SMTP_SSL(smtp_server, port=smtp_port)
#     debug_level = 1
#     mail_server.set_debuglevel(debug_level)

#     # if sender_password:
#     #     mail_server.login(user=self.sender, password=self.sender_password)

#     #     self.mail_server = mail_server

#     # else:
#     mail_pass = getpass.getpass('Password for user: {} '.format(sender))
#     mail_server.login(user=sender, password=mail_pass)

#     mail_server.send_message(message)
#     print(mail_server)
#     mail_server.quit()





def send(message):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()
