import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

students = {
    'Age': [21, 22, 23, 22, 23],
    'GPA'  : [2.9, 3.4, 3.1, 3.4, 2.5],
    'No' : [30, 54, 69, 26, 77]
}
frame = pd.DataFrame(students)

corr = frame.corr()
sb.heatmap(corr, vmax=4.0, square=True)
plt.show()