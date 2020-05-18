import csv


def check_values():
    with open('search.csv', mode='r', encoding='utf8') as f:
        reader = csv.reader(f)
        for row in reader:
            start, stop, source = row
            start, stop = map(convert_date_to_number, (start, stop))
            if not start:
                start = 0
            if not stop:
                stop = 100000000
            if start > stop:
                start, stop = stop, start
            if not source:
                source = 'all'
        return start, stop, source


def convert_date_to_number(date):
    """

    :param date: a date in format 2020-04-05
    :return: a integer number  for this date 20200405
    """
    if not date:
        return date
    split_date = date.split('-')
    return int(''.join(split_date))