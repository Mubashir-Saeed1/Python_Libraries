import matplotlib.pyplot as plt

companies = ['Nokia', 'Samsung', 'Apple', 'Xiaomi', 'Huawei']
income = [20, 25, 30, 10, 15]
plt.pie(income, labels=companies, autopct='%1.1f%%', shadow=True, startangle=90)
plt.show()