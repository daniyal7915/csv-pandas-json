import json
import pandas as pd
from os.path import join, dirname, realpath


class Container:
    """Data container for testing"""
    directory = dirname(realpath(__file__))

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
        output = {}

        for i in range(1, 5):
            output[self.contained_names[0][i-1]] = pd.read_csv(join(self.directory, "files", f"{i+variant}.csv"))

        return output

    @property
    def contained_paths(self):
        output = []

        for key, value in {1: 'files', 4: 'files', 2: 'filez', 9: 'files', 10: 'files'}.items():
            output.append(join(self.directory, f'{value}', f'{key}.csv'))

        return output

    @property
    def contained_get_data(self):
        output = [1 for i in range(0, 12)]
        output[7] = None
        output = output + [[1, 1, 1, 1, '.json'], [1, 1, 1, 1, '.json'], None, {'courses': 1, 'students': 1,
                                                                                'tests': 1, 'marks': 1}]

        return output

    @property
    def contained_weight_all(self):
        return [self.contained_df(), self.contained_df(8), None]

    def contained_prepare_data(self, variant=0):
        output = {}

        for i in range(13, 15):
            output[self.contained_names[1][i - 13]] = pd.read_csv(join(self.directory, "files", f"{i+variant}.csv"))

        output['students'] = output['students'][['id', 'name', 'totalAverage', 'courses']]
        output['merged'] = output['merged'][['id_x', 'name', 'teacher', 'id_y', 'course_id', 'weight',
                                             'test_id', 'student_id', 'courseAverage']]

        return output

    @property
    def contained_output_data(self):
        output = []

        for i in range(17, 19):
            with open(join(self.directory, "files", f"{i}.json")) as infile:
                output.append(json.load(infile))

        return output
