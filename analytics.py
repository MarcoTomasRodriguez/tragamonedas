import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('shoots.csv', header=None)
numbers = df.to_numpy().flatten()

unique, counts = np.unique(numbers, return_counts=True)

fig, ax = plt.subplots()
ax.pie(counts, labels=unique, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')
plt.savefig("report.pdf")