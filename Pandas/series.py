import pandas as pd

student = pd.Series(["Mubashir", "Hassan", "Qaisar", "Jamshid", "Zeeshan"], index= [1630, 1669, 1627, 1654, 4477])
print(student)

print(student[1630])
print(student.values)
print(student.index)

student1 = pd.Series([1630, 1669, 1627, 1654, 4477], index= ["Mubashir", "Hassan", "Qaisar", "Jamshid", "Zeeshan"])
print(student1[student1<1669])

print("Qaisar" in student.values)
print("Qaisar" in student1.index)

print(student.isnull())
print(student.notnull())
