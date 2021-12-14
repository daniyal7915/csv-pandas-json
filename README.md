CSV to JSON converter using pandas for data processing.

The converter receives paths to  courses, students, tests, marks .csv files and
a .json file as command-line arguments. 

If the paths are valid, the program creates a .json file from already existing 
.csv files, listing all students with their IDs, names, average marks for 
all courses and the personalized list of courses where a student has had at 
least one test. The course information includes ID, name, instructor 
and average mark.