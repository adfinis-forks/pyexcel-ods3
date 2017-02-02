import os
from pyexcel_ods3.ods import ODSWriter as Writer, ODSBook as Reader
from base import PyexcelWriterBase, PyexcelHatWriterBase


class TestNativeODSWriter:
    def test_write_book(self):
        self.content = {
            "Sheet1": [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]],
            "Sheet2": [[4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6]],
            "Sheet3": [[u'X', u'Y', u'Z'], [1, 4, 7], [2, 5, 8], [3, 6, 9]]
        }
        self.testfile = "writer.ods"
        writer = Writer()
        writer.open(self.testfile)
        writer.write(self.content)
        writer.close()
        reader = Reader()
        reader.open(self.testfile)
        content = reader.read_all()
        reader.close()
        for key in content.keys():
            content[key] = list(content[key])
        assert content == self.content

    def tearDown(self):
        if os.path.exists(self.testfile):
            os.unlink(self.testfile)


class TestodsnCSVWriter(PyexcelWriterBase):
    def setUp(self):
        self.testfile = "test.ods"
        self.testfile2 = "test.csv"

    def tearDown(self):
        if os.path.exists(self.testfile):
            os.unlink(self.testfile)
        if os.path.exists(self.testfile2):
            os.unlink(self.testfile2)


class TestodsHatWriter(PyexcelHatWriterBase):
    def setUp(self):
        self.testfile = "test.ods"

    def tearDown(self):
        if os.path.exists(self.testfile):
            os.unlink(self.testfile)
