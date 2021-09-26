import pandas as pd
from pandas.core.reshape.concat import concat

data1 = {"Name": ["Hassan", "Mubashir", "Jamshid", "Zeeshan"], "Age": [22, 21, 21, 23]}
data2 = {
    "Name": ["Hassan", "Mubashir", "Jamshid", "Zeeshan"],
    "GPA": [2.2, 2.1, 2.1, 2.3],
}

frame1 = pd.DataFrame(data1)
frame2 = pd.DataFrame(data2)

print(concat([frame1, frame2], axis= 0))