""" Classifies email """

import csv

def classify_by_error_code(diag_code):
    """
    Classify the email via smtp errors. Smtp errors codes are mapped
    with classification
    """
    error = check_basic_codes(None, diag_code)
    if any(error):
        enhanced_codes = check_enchaned_status_codes(None, error['code'])
        if any(enhanced_codes):
            error = enhanced_codes
    return error

def check_basic_codes(path=None, diag_code=''):
    """
    Checks the diagnostic code in the basic error codes by path provided
    """
    if diag_code is None:
        return {}

    if path is None:
        path = 'basic_error_codes.csv'
    basic_error_codes = {}
    with open(path, mode='r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            basic_code = row[0]
            if basic_code in diag_code:
                basic_error_codes = {
                    "code": basic_code,
                    "description": row[1],
                    "flag_as": row[2]
                }

    return basic_error_codes

def check_enchaned_status_codes(path=None, basic_error_code=None):
    """
    This check the basic code againts the exhaustive list of enhanced smtp reply codes
    https://www.iana.org/assignments/smtp-enhanced-status-codes/smtp-enhanced-status-codes.xhtml
    Be sure to edit the csv file to set the flag values
    """
    if basic_error_code is None:
        return {}

    enhanced_codes = {}
    if path is None:
        path = 'smtp-enhanced-status-codes-3.csv'
    with open(path, mode='r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            # Build the basic_error_code.x.x
            associated_basic_code = row[2]
            if associated_basic_code == 'Any' or basic_error_code in associated_basic_code:
                full_smtp_code = basic_error_code + ' ' + row[0].replace('X', basic_error_code[0])
                if full_smtp_code != '{0} {1}.0.0'.format(basic_error_code, basic_error_code[0]):
                    print full_smtp_code
                    enhanced_codes = {
                        'code': full_smtp_code,
                        'description': row[3].replace('\n', ' '),
                        'flag_as': row[7]
                    }
                    break
    return enhanced_codes
