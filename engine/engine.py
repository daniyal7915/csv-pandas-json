import sys
import pandas as pd
import json


class GetData:
    """Get data from input files"""
    template = ['courses.csv', 'students.csv', 'tests.csv', 'marks.csv', '.json']
    output_path = None

    def get_paths(self):
        """Check and set file paths"""
        try:
            paths = sys.argv[1:]

            if [paths[0][-11:], paths[1][-12:], paths[2][-9:], paths[3][-9:], paths[4][-5:]] == self.template:
                return paths

        except (IndexError, TypeError):
            pass

    def set_dtype(self, file):
        """Set and return a data type argument for df.astype"""
        dtype = 'int'

        if file in self.template[0:2]:
            dtype = {'id': dtype}

        return dtype

    def csv_to_df(self, path, file=None):
        """Create dataframe from csv"""
        try:
            df = pd.read_csv(path)
            df.astype(self.set_dtype(file))
            return df
        except (FileNotFoundError, ValueError, pd.errors.IntCastingNaNError):
            pass

    def get_data(self):
        """Return a dict with created dataframes"""
        paths = self.get_paths()

        if paths:
            courses = self.csv_to_df(paths[0], 'courses.csv')
            students = self.csv_to_df(paths[1], 'students.csv')
            tests = self.csv_to_df(paths[2])
            marks = self.csv_to_df(paths[3])

            if courses is not None and students is not None and tests is not None and marks is not None:
                self.output_path = paths[4]
                return {'courses': courses, 'students': students, 'tests': tests, 'marks': marks}


class CheckData(GetData):
    """Check data"""

    def check_weight(self):
        """Check if weight of all tests in each course is equal to 100"""
        data = self.get_data()

        if data:
            if data['tests'].groupby('course_id')['weight'].sum().mean() != 100:
                return

            return data

    def check_all(self):
        """Check if 0 <= marks <= 100 in the marks dataframe. Call teh weight check """
        data = self.check_weight()

        if data:
            marks = data['marks']['mark']

            if marks.min() < 0 or marks.max() > 100:
                return

            return data


class Output(CheckData):
    """Create Output"""
    output = {"error": "Invalid course weights"}

    def prepare_data(self, data):
        """Insert two additional columns into students; merge courses, tests, marks;
           recalculate marks. Delete redundant data. Return prepared data"""
        data['students'].insert(2, 'totalAverage', 0)
        data['students'].insert(3, 'courses', 0)

        tests_marks = pd.merge(data['tests'], data['marks'], left_on='id', right_on='test_id', how='inner')
        data['merged'] = pd.merge(data['courses'], tests_marks, left_on='id', right_on='course_id', how='inner')

        data['merged']['mark'] = data['merged']['mark'] * data['merged']['weight'] / 100
        data['merged'].rename({'mark': 'courseAverage'}, axis=1, inplace=True)

        for name in ['courses', 'tests', 'marks']:
            del data[name]

        return data

    def output_data(self, data):
        """Create output data"""
        data = self.prepare_data(data)

        output = {'students': data['students'].to_dict(orient='records')}

        for student in output['students']:
            df = data['merged'].loc[data['merged']['student_id'] == student['id']]
            df = df[['course_id', 'name', 'teacher', 'courseAverage']]
            df = df.groupby(['course_id', 'name', 'teacher'])['courseAverage'].sum().reset_index()
            df['courseAverage'] = df['courseAverage'].apply(lambda x: round(x, 2))
            student['courses'] = df.to_dict(orient='records')
            student['totalAverage'] = round(df['courseAverage'].mean(), 2)

        return output

    def create_output(self):
        """Create .json"""
        checked_data = self.check_all()

        if checked_data:
            self.output = self.output_data(checked_data)

        try:
            with open(self.output_path, "w") as outfile:
                outfile.write(json.dumps(self.output, indent=4))
        except (FileNotFoundError, TypeError):
            pass
