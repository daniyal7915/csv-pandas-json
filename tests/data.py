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
        return [['courses', 'students', 'tests', 'marks'], ['students', 'merged']]

    def contained_df(self, variant=0):
        dfs = {}

        for i in range(1, 5):
            dfs[self.contained_names[0][i-1]] = pd.read_csv(os.path.join("files", f"{i+variant}.csv"))

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

    def contained_prepare_data(self, variant=0):
        dfs = {}

        for i in range(13, 15):
            dfs[self.contained_names[1][i - 13]] = pd.read_csv(os.path.join("files", f"{i+variant}.csv"))

        dfs['students'] = dfs['students'][['id', 'name', 'totalAverage', 'courses']]
        dfs['merged'] = dfs['merged'][['id_x', 'name', 'teacher', 'id_y', 'course_id', 'weight',
                                      'test_id', 'student_id', 'mark']]

        return dfs

    @property
    def contained_create_output(self):
        return [1, None, 1, 1, 1, 1, 1, 1, f'{os.path.join("files", "17.csv")}', 1,
                f'{os.path.join("filez", "17.csv")}', None]

    @property
    def contained_output_data(self):
        return [{'students': [{'courses': [{'courseAverage': 90.1,
                                            'course_id': 1,
                                            'name': 'Biology',
                                            'teacher': 'Mr. D'},
                                           {'courseAverage': 51.8,
                                            'course_id': 2,
                                            'name': 'History',
                                            'teacher': ' Mrs. P'},
                                           {'courseAverage': 74.2,
                                            'course_id': 3,
                                            'name': 'Math',
                                            'teacher': ' Mrs. C'}],
                               'id': 1,
                               'name': 'A',
                               'totalAverage': 72.03},
                              {'courses': [{'courseAverage': 50.1,
                                            'course_id': 1,
                                            'name': 'Biology',
                                            'teacher': 'Mr. D'},
                                           {'courseAverage': 74.2,
                                            'course_id': 3,
                                            'name': 'Math',
                                            'teacher': ' Mrs. C'}],
                               'id': 2,
                               'name': 'B',
                               'totalAverage': 62.15},
                              {'courses': [{'courseAverage': 90.1,
                                            'course_id': 1,
                                            'name': 'Biology',
                                            'teacher': 'Mr. D'},
                                           {'courseAverage': 51.8,
                                            'course_id': 2,
                                            'name': 'History',
                                            'teacher': ' Mrs. P'},
                                           {'courseAverage': 74.2,
                                            'course_id': 3,
                                            'name': 'Math',
                                            'teacher': ' Mrs. C'}],
                               'id': 3,
                               'name': 'C',
                               'totalAverage': 72.03}]},
                {'students': [{'courses': [{'courseAverage': 1.3,
                                            'course_id': 1,
                                            'name': 'Biology',
                                            'teacher': 'Mr. D'},
                                           {'courseAverage': 51.8,
                                            'course_id': 2,
                                            'name': 'History',
                                            'teacher': ' Mrs. P'}],
                               'id': 5,
                               'name': 'D',
                               'totalAverage': 26.55}]}]
