import pandas as pd

students = {
    'regNo': ['18PWCSE1630', '18PWCSE1654', '18PWCSE1669', '18PWCSE1627', '18PWMEC4477'],
    'Name' : ['Mubashir', 'Jamshid', 'Hassan', 'Qaisar', 'Zeeshan'],
    'GPA'  : [2.9, 3.4, 3.1, 3.4, 2.5]
}

frame = pd.DataFrame(students, index=(1, 2, 3, 4, 5))

def fun(mar):
    return mar - 0.1

print(frame['GPA'].apply(fun))