import ctypes


class Array:

    def __init__(self, size):
        """
        Creates the array with specific size using the ctypes module.
        """
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.set_values(None)

    def __len__(self):
        """
        Returns the length of the array.
        :return: int
        """
        return self._size

    def set_values(self, value):
        """
        Sets specific value to all the elements in the array.
        :param value: value
        :return: None
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __getitem__(self, index):
        """
        Gets the contents of the index element.
        :param index: int
        :return: content of the element.
        """
        assert 0 <= index < len(self), "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        Puts the value in the array element at index position.
        :param value: value
        :return: None
        """
        assert 0 <= index < len(self), "Array subscript out of range"
        self._elements[index] = value

    # Returns the array's iterator for traversing the elements.
    def __iter__(self):
        return _ArrayIterator(self._elements)

    def __str__(self):
        """
        Array representation.
        :return: str
        """
        res = '['
        for el in self._elements:
            res += str(el) + ', '
        res = res[:-2] + ']'
        return res

# An iterator for the Array ADT.


class _ArrayIterator:
    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration


class Array2D:
    """
    Creates a 2-D array of size numRows x numCols.
    """

    def __init__(self, num_rows, num_cols):
        """
        Creates the 2-D array of the specific size: num_rows and num_cols.
        """
        self.rows = Array(num_rows)
        for i in range(num_rows):
            self.rows[i] = Array(num_cols)

    def num_rows(self):
        """
        Returns the number of rows in the 2-D array.
        :return: int
        """
        return len(self.rows)

    def num_cols(self):
        """
        Returns the number of columns in the 2-D array.
        :return: int
        """
        return len(self.rows[0])

    def set_value(self, value):
        """
        Sets specific value to all the elements in the array.
        :return: None
        """
        for row in self.rows:
            row.set_values(value)

    def __getitem__(self, index_tuple):
        """
        Gets the contents of the element at position [i, j].
        :param index_tuple: tuple
        :return: content of the element.
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row, col = index_tuple
        assert 0 <= row < self.num_rows() and 0 <= col < self.num_cols(), \
            "Array subscript out of range."
        array_1d = self.rows[row]
        return array_1d[col]

    def __setitem__(self, index_tuple, value):
        """
        Sets the contents of the element at position [i,j] to value.
        :param index_tuple: tuple
        :param value: value
        :return: None
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row, col = index_tuple
        assert 0 <= row < self.num_rows() and 0 <= col < self.num_cols(), \
            "Array subscript out of range."
        array_1d = self.rows[row]
        array_1d[col] = value

    def __str__(self):
        res = '[\n'
        for row in array2.rows:
            res += str(row) + '\n'
        return res + ']'


if __name__ == '__main__':
    # Testing Array
    array1 = Array(10)
    # print(array1)
    assert array1.__len__() == 10
    array1.set_values(95)
    # print(array1)
    for index in range(10):
        assert array1.__getitem__(index) == 95
    array1.__setitem__(3, 51)
    # print(array1)
    assert array1.__getitem__(3) == 51

    # Testing Array 2D
    array2 = Array2D(5, 4)
    assert array2.num_rows() == 5
    assert array2.num_cols() == 4
    # print(array2)
    array2.set_value(95)
    # print(array2)
    assert array2.__getitem__((3, 3)) == 95
    array2.__setitem__((2, 2), 20)
    # print(array2)
    assert array2.__getitem__((2, 2)) == 20