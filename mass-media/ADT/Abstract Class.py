import json
from ADT import Array, Array2D


class Structure:
    def __init__(self, num_rows, num_cols):
        """
        Creates the structure.
        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        self._structure = Array2D(num_rows, num_cols)

    def num_rows(self):
        """
        Returns the number of rows in the structure.
        :return: the number rows in the structure.
        """
        return self._structure.num_rows()

    def num_cols(self):
        """
        Returns the number of columns in the structure.
        :return: the number of columns in the structure.
        """
        return self._structure.num_cols()

    def set_item(self, row, col, value):
        """
        Sets the indicated item to the specific value.
        :param row: row of the item
        :param col: column of the item
        :param value: value
        :return: None
        """
        self._structure[row, col] = value

    def set_row(self, row, value):
        """
        Sets the indicated row to the specific value.
        :param row: row
        :param value: value
        :return: None
        """
        for i, el in enumerate(value):
            self.set_item(row, i, el)

    def get_item(self, row, col):
        """
        Gets the indicated item.
        :param row: row of the item
        :param col: column of the item
        :return: None
        """
        return self._structure[row, col]

    def get_row(self, row):
        """
        Gets the indicated row
        :param row: row
        :return: string
        """
        result = ''
        for i in range(self.num_cols()):
            result += str(self._structure[row, i]) + '   '
        return result

    def search_by_source(self, source):
        """
        Search the articles with the specific source.
        :param source: string
        :return: string
        """
        result = ''
        for i in range(self.num_rows()):
            if self._structure[i, 1] == source:
                result += self.get_row(i) + '\n'
        return result

    def search_by_date(self, date):
        """
        Search the articles with the specific date.
        :param date: string
        :return: string
        """
        result = ''
        for i in range(self.num_rows()):
            if self._structure[i, 0] == date:
                result += self.get_row(i) + '\n'
        return result

    def search_by_source_and_date(self, source, date):
        """
        Search the articles with the specific source and date.
        :param source: string
        :param date: string
        :return: string
        """
        result = ''
        for i in range(self.num_rows()):
            if self._structure[i, 1] == source:
                if self._structure[i, 0] == date:
                    result += self.get_row(i) + '\n'
        return result

    def __str__(self):
        """
        Structure representation.
        :return: None
        """
        table = ''
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                table += self._structure[i, j] + ', '
            table += '\n'
        return table


def check_present_content(value):
    if value is None:
        value = 0
    return value


def article_categorizer(entry):
    time = check_present_content(entry['publishedAt'][:10])
    source = check_present_content(entry['source']['name'])
    title = check_present_content(entry['title'])
    url = check_present_content(entry['url'])
    return time, source, title, url


def structure_info(file):
    """
    Function that structures our info
    :param file: str
    :return: list
    """
    num_of_sections = 4
    result = list()
    with open(file, mode='r', encoding='utf-8') as f:
        articles = json.load(f)['articles']
        for entry in articles:
            news_arr = Array(num_of_sections)
            time, source, title, url = article_categorizer(entry)
            news_arr[0], news_arr[1], news_arr[2], news_arr[3] = time, source, title, url
            result.append(news_arr)
    return result


def display_table(file_name):
    """
    Function that displays our info in a simple table format
    :param file_name: str
    :return: list
    """
    table = Structure(len(structure_info(file_name)), 6)
    counter = 0
    for lst in structure_info(file_name):
        table.set_row(counter, lst)
        counter += 1
    return table


if __name__ == '__main__':
    table_1 = display_table('gb .json')
    # print(len(structure_info('gb .json')))
    print(table_1.search_by_source('Independent'))
    print(table_1.search_by_date('2020-04-18'))
    print(table_1.search_by_source_and_date('Independent','2020-04-18'))
