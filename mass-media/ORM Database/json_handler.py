import json


def check_response(json_data):
    if json_data['status'] != 'ok' or json_data["totalResults"] < 1:
        return False
    return True


def check_present_content(value):
    if value is None:
        value = 0
    return value


def article_categorizer(entry):
    time = check_present_content(entry['publishedAt'][:10])
    date_as_number = convert_date_to_number(time)
    source = check_present_content(entry['source']['name'])
    title = check_present_content(entry['title'])
    url = check_present_content(entry['url'])
    content = check_present_content(entry['content'])
    return date_as_number, time, source, title, url, content


def convert_date_to_number(date):
    """

    :param date: a date in format 2020-04-05
    :return: a integer number  for this date 20200405
    """
    if not date:
        return date
    split_date = date.split('-')
    return int(''.join(split_date))

