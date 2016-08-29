import re
import time
from datetime import datetime


def contains_one_of_list(source, list):
    for l in list:
        if l.lower() in source.lower():
            return True
    return False

# def convert_to_date_obj(date_str):
#     if date_str


def valid_date(datestring):
    try:
        mat = re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', datestring)
        if mat is not None:
            a = datetime(*(map(int, mat.groups()[-1::-1])))
            print(a)
            return True
    except ValueError:
        pass
    return False