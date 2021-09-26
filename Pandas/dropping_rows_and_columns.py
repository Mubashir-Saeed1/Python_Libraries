import pandas as pd

students = {
    'regNo': ['18PWCSE1630', '18PWCSE1654', '18PWCSE1669', '18PWCSE1627', '18PWMEC4477'],
    'Name' : ['Mubashir', 'Jamshid', 'Hassan', 'Qaisar', 'Zeeshan'],
    'GPA'  : [2.9, 3.4, 3.1, 3.4, 2.5]
}

frame = pd.DataFrame(students, index=(1, 2, 3, 4, 5))

#Dropping Row
print(frame.drop(4, inplace= False)) #inplace = True will not create a new copy and will modify the original DataFrame
print(frame)

#Dropping Column
print(frame.drop('GPA', axis= 1, inplace= True)) #Original DataFrame Modified
print (frame)