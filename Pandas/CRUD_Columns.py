import pandas as pd

students = {
    'regNo': ['18PWCSE1630', '18PWCSE1654', '18PWCSE1669', '18PWCSE1627', '18PWMEC4477'],
    'Name' : ['Mubashir', 'Jamshid', 'Hassan', 'Qaisar', 'Zeeshan'],
    'GPA'  : [2.9, 3.4, 3.1, 3.4, 2.5]
}

frame = pd.DataFrame(students, index=(1, 2, 3, 4, 5))

#Reading Columns
print(frame.loc[2]) #Locate using our index
print(frame.iloc[2]) #Locate using Default index

#Creating new Column
frame['Age'] = [21, 21, 22, 22, 22]
print(frame)

#Deleting Column
del frame['Age']
print(frame)

#Updating value in a Column
frame.at[4, 'GPA'] = 3.3
print(frame)