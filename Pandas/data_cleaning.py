import pandas as pd

students = {
    'regNo': ['18PWCSE1630', '18PWCSE1654', '18PWCSE1669', '18PWCSE1627', '18PWMEC4477'],
    'Name' : ['Mubashir', 'Jamshid', 'Hassan', 'Qaisar', 'Zeeshan'],
    'GPA'  : [2.9, pd.NA, pd.NA, pd.NA, 2.5]
}

frame = pd.DataFrame(students, index=(1, 2, 3, 4, 5))

#To drop NA Values
print(frame.dropna(how='all')) #Delete Row if it is completely NA
print(frame.dropna()) #Delete Row if it has at least one NA

print(frame.dropna(how = 'all', axis= 1)) #To delete Column
print(frame.dropna(thresh= 1)) #No. of at least fields that should have data
print(frame.dropna(thresh=4)) #Will delete entire frame

#To fill NA Values
print(frame.fillna(3.0))
print(frame.ffill()) #Forward Fill
print(frame.bfill()) #Backward Fill
print(frame.fillna({'GPA': 3.0})) #To specify a Column

students = {
    'regNo': ['18PWCSE1630', '18PWCSE1654', '18PWCSE1669', '18PWCSE1627', '18PWMEC4477'],
    'Name' : ['Mubashir', 'Jamshid', 'Hassan', 'Qaisar', 'Zeeshan'],
    'GPA'  : [2.9, 3.4, 3.1, 3.4, 2.5]
}

frame = pd.DataFrame(students, index=(1, 2, 3, 4, 5))
print(frame)

#Duplicated
print(frame.duplicated())
print(frame.duplicated(['GPA']))
print(frame.drop_duplicates(['GPA']))
print(frame.drop_duplicates(['GPA'], keep= 'last'))