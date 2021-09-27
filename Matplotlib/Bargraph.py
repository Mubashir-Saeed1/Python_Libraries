import matplotlib.pyplot as plt

companies = ['Nokia', 'Samsung', 'Apple', 'Xiaomi', 'Huawei']
income = [230000, 320000, 340000, 221000, 350000]
x = [i for i,v in enumerate(companies, 1)]

plt.bar(x, income, color= 'red', width=0.4) #Default width is 0.8
plt.xlabel = companies
plt.ylabel = income
plt.title = 'Income of various Companies'
plt.xticks(x, companies)
plt.show()
