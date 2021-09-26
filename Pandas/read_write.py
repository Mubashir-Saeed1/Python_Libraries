import pandas as pd

#Reading File from Directory
frame = pd.read_csv('eval.csv')
print(frame)
print("Head: ", frame.head())
print("Tail: ", frame.tail())
print("Columns: ", frame.columns)
print("Genders: ", frame['sex'])
print("Males Information: ", frame[frame['sex'] == 'male'])

#Creating new File
students = {
    'regNo': ['18PWCSE1630', '18PWCSE1654', '18PWCSE1669', '18PWCSE1627', '18PWMEC4477'],
    'Name' : ['Mubashir', 'Jamshid', 'Hassan', 'Qaisar', 'Zeeshan'],
    'GPA'  : [2.9, 3.4, 3.1, 3.4, 2.5]
}

frame = pd.DataFrame(students, index=(1, 2, 3, 4, 5))
frame.to_csv('students.csv')

file = pd.read_csv('students.csv')
print(file)