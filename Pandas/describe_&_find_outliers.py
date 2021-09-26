import pandas as pd

age = [23, 21, 34, 56, 35, 65, 64, 36, 76, 93, 48, 57, 38]
frame = pd.DataFrame({'Ages': age})
print(frame.describe())

print(frame[frame['Ages']>80]) #To find the outliers