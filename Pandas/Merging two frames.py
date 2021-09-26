import pandas as pd

data1 = {"Name": ["Hassan", "Mubashir", "Jamshid", "Zeeshan"], "Age": [22, 21, 21, 23]}
data2 = {
    "Name": ["Hassan", "Mubashir", "Jamshid", "Zeeshan"],
    "GPA": [2.2, 2.1, 2.1, 2.3],
}

frame1 = pd.DataFrame(data1)
frame2 = pd.DataFrame(data2)
frame = pd.merge(frame1, frame2)
print(frame)

data1 = {
    "Name": ["Hassan", "Mubashir", "Jamshid", "Zeeshan", "Sameer"],
    "Age": [22, 21, 21, 23, 20],
}
data2 = {
    "Name": ["Hassan", "Mubashir", "Jamshid", "Zeeshan", "Qaisar"],
    "GPA": [2.2, 2.1, 2.1, 2.3, 2.3],
}

frame1 = pd.DataFrame(data1)
frame2 = pd.DataFrame(data2)

print(pd.merge(frame1, frame2))  # No extra data will be picked
print(pd.merge(frame1, frame2, how="left"))  # Only data from left frame will be picked
print(
    pd.merge(frame1, frame2, how="right")
)  # Only data from the right frame will be picked
print(pd.merge(frame1, frame2, how="outer"))  # Data from both the frames will be picked
