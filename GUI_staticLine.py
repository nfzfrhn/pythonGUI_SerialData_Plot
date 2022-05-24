#static_plot.py

import matplotlib.pyplot as plt

#data
data_1st = [60, 59, 49, 51, 49, 52, 53]

# Create the figure and axis objects
fig, ax = plt.subplots()

# Plot the data and customize
ax.plot(data_1st)
ax.set_xlabel('Day number')
ax.set_ylabel('Temperature(*F)')
ax.set_title('Temperature in Portland or over 7 days')

plt.show()
