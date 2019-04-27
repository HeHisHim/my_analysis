import matplotlib.pyplot as plt
import math

x_cube_values = list(range(1, 500))
y_cube_values = [math.pow(x, 3) for x in x_cube_values]

plt.scatter(x_cube_values, y_cube_values, c = y_cube_values, s = 1)

plt.title("Cube Value", fontsize = 25)
plt.xlabel("values", fontsize = 15)
plt.ylabel("Cube Values", fontsize = 15)

plt.tick_params(axis = "both", labelsize = 15)
plt.axis([0, x_cube_values[-1], 0, math.pow(x_cube_values[-1], 3)])

plt.show()