#!/usr/bin/env python3
import os
import datetime
import reports
from run import process_txtfile, collect_txtfiles

description_loc = 'supplier-data/descriptions'


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
    attachment = 'processed.pdf'
    current_date = datetime.datetime.today().strftime("%B, %d %Y")
    
    title = 'Processed update on {}'.format(current_date)
    paragraph = prepare_desc()  #file_dict['description']

    reports.generate_report(attachment, title, paragraph)