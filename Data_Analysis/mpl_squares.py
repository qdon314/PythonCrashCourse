import matplotlib.pyplot as plt

input_values = range(1, 1001)
squares = [x**2 for x in input_values]

plt.style.use(plt.style.available[0])
fig, ax = plt.subplots()
ax.scatter(input_values, squares, c=squares, cmap=plt.cm.Blues, s=100)

# Set chart title and labels.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()