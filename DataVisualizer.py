import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 15, 25, 30]
}
df = pd.DataFrame(data)
fig = px.scatter(df, x='x', y='y')
fig.show()

#Line Graph
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.show()

#Bar Graph
a = ['A', 'B', 'C', 'D']
b = [10, 20, 15, 25]
plt.bar(a, b)
plt.show()

#Pie Chart
labels = 'A', 'B', 'C', 'D'
sizes = [15, 30, 45, 10]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()

