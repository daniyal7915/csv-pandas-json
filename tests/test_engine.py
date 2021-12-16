import sys
from unittest import main, mock, TestCase
from engine.engine import GetData, CheckData, Output
from tests.data import Container

check = CheckData()
output = Output()


class TestGetData(TestCase, Container, GetData):
    """Test GetData class"""

    def test_get_paths(self):
        """Test the get_paths method"""
        for key, value in self.contained_cl_arguments.items():
            with self.subTest(n=key):
                with mock.patch.object(sys, 'argv', value):
                    if key == 1:
                        self.assertEqual(self.get_paths(), self.template)
                    else:
                        self.assertFalse(self.get_paths())

    def test_set_dtype(self):
        """Test the set_dtype method"""
        count = 0

        for key, value in self.contained_dtype[2].items():
            count += 1
            with self.subTest(n=count):
                self.assertEqual(self.set_dtype(key), self.contained_dtype[value])

    @mock.patch('engine.engine.GetData.set_dtype')
    def test_csv_to_df(self, dtype):
        """Test the csv_to_df method"""
        dtype.side_effect = self.contained_dtype[:-1][::-1] + [self.contained_dtype[1]]*3
        names = [self.contained_names[0], self.contained_names[3]]

        for i in range(2):
            with self.subTest(n=i):
                self.assertTrue(self.csv_to_df(self.contained_paths[i]).equals(self.contained_df()[names[i]]))

        for i in range(2, 5):
            with self.subTest(n=i):
                self.assertFalse(self.csv_to_df(self.contained_paths[i]))

    @mock.patch('engine.engine.GetData.get_paths')
    @mock.patch('engine.engine.GetData.csv_to_df')
    def test_get_data(self, csv_df, get_paths):
        """Test the get_data method"""
        csv_df.side_effect = self.contained_get_data[:12]
        get_paths.side_effect = self.contained_get_data[12:15]

        self.assertFalse(self.output_path)
        self.assertEqual(self.get_data(), self.contained_get_data[-1])
        self.assertEqual(self.output_path, self.contained_get_data[12][4])

        for i in range(4, 6):
            with self.subTest(n=i):
                self.assertFalse(self.get_data())











































main()
