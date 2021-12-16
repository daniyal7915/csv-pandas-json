import os
import pandas as pd


class Container:
    """Data container for testing"""

    @property
    def contained_cl_arguments(self):
        return {1: ['.py', 'courses.csv', 'students.csv', 'tests.csv', 'marks.csv', '.json'],
                2: ['students.csv', 'courses.csv', 'tests.csv', 'marks.csv', '.json'],
                3: None}

    @property
    def contained_dtype(self):
        return ['int', {'id': 'int'}, {None: 0, 'courses.csv': 1, 'students.csv': 1}]

    @property
    def contained_names(self):
        return ['courses', 'students', 'tests', 'marks']

    def contained_df(self, variant=0):
        dfs = {}

        for i in range(1, 5):
            dfs[self.contained_names[i-1]] = pd.read_csv(os.path.join("files", f"{i+variant}.csv"))

        return dfs

    @property
    def contained_paths(self):
        return [f'{os.path.join("files", "1.csv")}', f'{os.path.join("files", "4.csv")}',
                f'{os.path.join("filez", "2.csv")}', f'{os.path.join("files", "9.csv")}',
                f'{os.path.join("files", "10.csv")}']

    @property
    def contained_get_data(self):
        output = [1 for i in range(0, 12)]
        output[7] = None
        output = output + [[1, 1, 1, 1, '.json'], [1, 1, 1, 1, '.json'], None,
                           {'courses': 1, 'students': 1, 'tests': 1, 'marks': 1}]
        return output

    @property
    def contained_weight_all(self):
        return [self.contained_df(), self.contained_df(8), None]














