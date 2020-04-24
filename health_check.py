#!/usr/bin/env python3
"""script will monitor some of your system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script should send an email if there are problems, such as:

Report an error if CPU usage is over 80%
Report an error if available disk space is lower than 20%
Report an error if available memory is less than 500MB
Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
Create a python script named health_check.py using the nano editor:
"""

#TODO: Complete the script to check the system statistics every 60 seconds, and in event of any issues detected among the ones mentioned above, an email should be sent with the following content:
"""
From: automation@example.com
To: username@example.com
Replace username with the username given in the Connection Details Panel on the right hand side.
Subject line:

Case | Subject line
CPU usage is over 80% | Error - CPU usage is over 80%
Available disk space is lower than 20% | Error - Available disk space is less than 20%
available memory is less than 500MB | Error - Available memory is less than 500MB
hostname "localhost" cannot be resolved to "127.0.0.1" | Error - localhost cannot be resolved to 127.0.0.1

E-mail Body: Please check your system and resolve the issue as soon as possible.
Note: There is no attachment file here, so you must be careful while defining the generate_email() method in the emails.py script or you can create a separate 
generate_error_report() method for handling non-attachment email.
"""


#!/usr/bin/env python3
import os
import sys
import shutil
import socket
import psutil
from emails import send_email

lab_user = "TODO: Insert here"



def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isn't enough disk space, False otherwise"""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def check_root_full():
    """Returns True if the root partition is full, False otherwise"""
    return check_disk_full(disk='/', min_gb=2, min_percent=20)

def check_cpu_constrained():
    """Returns True if the cpu is having too much usage, False otherwise."""
    return psutil.cpu_percent(1) > 80

def check_no_network():
    """Returns True if it fails to resolve Google's URL, False otherwise"""
    try:
        socket.gethostbyname("127.0.0.1")
        return False
    except:
        return True

def check_ram():
    #TODO: Create function that verifies there is more than 500MB free RAM
    size_bytes = psutil.virtual_memory().available
    # This 524million number is how many bytes are in 500MB
    return size_bytes > 524,288,000 

def generate_error_report(sender, recipient, subject, body):
    
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



  return message

def main():
    failed_checks = []
    checks = [
        (check_ram, "Error - Available memory is less than 500MB"),
        (check_root_full, "Error - Available disk space is less than 20%"),
        (check_no_network, "Error - localhost cannot be resolved to 127.0.0.1"),
        (check_cpu_constrained, "Error - CPU usage is over 80%")
    ]
    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            failed_checks.append(msg)
            everything_ok = False
            # sys.exit(1)

    if not everything_ok:
        email_body = "Please check your system and resolve the issue as soon as possible."
        email_subject = failed_checks
        sender = automation@example.com
        recipient = "{}@example.com".format(lab_user)
        error_report = generate_error_report(sender, recipient, email_subject, email_body)
        send_email(error_report)
        #sys.exit(1)

    print("Everything ok.")
    sys.exit(0)


main()