import pandas as pd

students = {
    'regNo': ['18PWCSE1630', '18PWCSE1654', '18PWCSE1669', '18PWCSE1627', '18PWMEC4477'],
    'Name' : ['Mubashir', 'Jamshid', 'Hassan', 'Qaisar', 'Zeeshan'],
    'GPA'  : [2.9, 3.4, 3.1, 3.4, 2.5]
}

frame = pd.DataFrame(students, index=(1, 2, 3, 4, 5))

print(frame)
print("Complete Head: \n", frame.head())
print("Complete Tail: \n", frame.tail())
print("First Two Values: ", frame.head(2))
print("Columns of Frame: ", frame.columns)
print("GPA Greater Than 3.0:, ", frame[frame['GPA']>3])
print("GPA: ", frame.GPA)