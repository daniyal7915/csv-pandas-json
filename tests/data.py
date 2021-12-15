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













