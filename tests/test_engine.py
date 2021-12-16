import sys
from unittest import main, mock, TestCase
from engine.engine import GetData, CheckData, Output
from tests.data import Container

data = GetData()
check = CheckData()
output = Output()


class TestGetData(TestCase, Container):
    """Test GetData class"""

    def test_get_paths(self):
        """Test the get_paths method"""
        for key, value in self.contained_cl_arguments.items():
            with self.subTest(test=key):
                with mock.patch.object(sys, 'argv', value):
                    if key == 1:
                        self.assertEqual(data.get_paths(), data.template)
                    else:
                        self.assertFalse(data.get_paths())

    def test_set_dtype(self):
        """Test the set_dtype method"""
        count = 0

        for key, value in self.contained_dtype[2].items():
            count += 1
            with self.subTest(test=count):
                self.assertEqual(data.set_dtype(key), self.contained_dtype[value])

    @mock.patch('engine.engine.GetData.set_dtype')
    def test_csv_to_df(self, dtype):
        """Test the csv_to_df method"""
        dtype.side_effect = self.contained_dtype[:-1][::-1] + [self.contained_dtype[1]]*3
        names = [self.contained_names[0][0], self.contained_names[0][3]]

        for i in range(2):
            with self.subTest(test=i):
                self.assertTrue(data.csv_to_df(self.contained_paths[i]).equals(self.contained_df()[names[i]]))

        for i in range(2, 5):
            with self.subTest(test=i):
                self.assertFalse(data.csv_to_df(self.contained_paths[i]))

    @mock.patch('engine.engine.GetData.get_paths')
    @mock.patch('engine.engine.GetData.csv_to_df')
    def test_get_data(self, csv_df, get_paths):
        """Test the get_data method"""
        csv_df.side_effect = self.contained_get_data[:12]
        get_paths.side_effect = self.contained_get_data[12:15]

        self.assertFalse(data.output_path)
        self.assertEqual(data.get_data(), self.contained_get_data[-1])
        self.assertEqual(data.output_path, self.contained_get_data[12][4])

        for i in range(4, 6):
            with self.subTest(test=i):
                self.assertFalse(data.get_data())


class TestCheckData(TestCase, Container):
    """Test CheckData class"""

    def process(self, func):
        """The process method for test_check_weight and test_check_all methods"""
        result = func()
        count = 0

        for name in self.contained_names[0]:
            count += 1
            with self.subTest(test=count):
                self.assertTrue(result[name].equals(self.contained_weight_all[0][name]))

        for i in range(5, 7):
            with self.subTest(test=i):
                self.assertFalse(func())

    @mock.patch('engine.engine.GetData.get_data')
    def test_check_weight(self, get_data):
        """Test the check_weight method"""
        get_data.side_effect = self.contained_weight_all

        self.process(check.check_weight)

    @mock.patch('engine.engine.CheckData.check_weight')
    def test_check_all(self, check_all):
        """Test the check_all method"""
        check_all.side_effect = self.contained_weight_all

        self.process(check.check_all)


class TestOutput(TestCase, Container):
    """Test Output class"""

    def test_prepare_data(self):
        """Test the prepare_data method"""
        result = output.prepare_data(self.contained_df())
        count = 0

        for name in self.contained_names[1]:
            count += 1
            with self.subTest(test=count):
                self.assertTrue(result[name].equals(self.contained_prepare_data()[name]))

    @mock.patch('engine.engine.Output.prepare_data')
    def test_output_data(self, prepared_data):
        prepared_data.side_effect = [self.contained_prepare_data(), self.contained_prepare_data(2)]

        for i in range(2):
            with self.subTest(test=i+1):
                self.assertEqual(output.output_data(1), self.contained_output_data[i])


if __name__ == "__main__":
    main()
