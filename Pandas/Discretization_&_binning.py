import pandas as pd

age = [23, 21, 34, 56, 35, 65, 64, 36, 76, 48, 57, 38]
bins = [18, 25, 35, 55, 70, 100]

categories = pd.cut(age, bins)
print(categories)
print(f'Categories {categories.categories}')
print("Codes: ", categories.codes)
print(pd.value_counts(categories))
