#!/usr/bin/env python3
import os
import datetime
import reports
from run import process_txtfile, collect_txtfiles
from emails import generate_email, send_email

description_loc = 'supplier-data/descriptions'
lab_user = 'TODO: INSERT THIS'

def prepare_desc():
    collected_files = collect_txtfiles(description_loc)
    full_description = ""
    for file in collected_files:
        dict_obj = process_txtfile(file)
        formatted_desc = """name: {}
                            weight: {} lbs

                        """.format(dict_obj['name'], dict_obj['weight'])
        full_description += formatted_desc
    return full_description

# DESIRED DESCRIPTION FORMAT BELOW
# name: Apple
# weight: 500 lbs
# [blank line]
# name: Avocado
# weight: 200 lbs
# [blank line]
# ...


if __name__ == "__main__":
    # Prepare PDF file report
    attachment = 'processed.pdf'
    current_date = datetime.datetime.today().strftime("%B, %d %Y")
    
    title = 'Processed update on {}'.format(current_date)
    paragraph = prepare_desc()  #file_dict['description']

    reports.generate_report(attachment, title, paragraph)

    # Create Email and send it
    sender = "automation@example.com"
    recipient = "{}@example.com".format(lab_user)
    email_subject = "Upload Completed - Online Fruit Store"
    email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    email_message = generate_email(sender, recipient, email_subject, email_body, attachment)
    send_email(email_message)