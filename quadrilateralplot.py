import matplotlib.pyplot as plt
# You should have matplotlib module in order to work with this code
# if you don't have matplotlib module
# pip install matplotlib 

# This script will plot the quadrilateral

values = eval(input()) # input the values of the quadrilateral just like the2 inputs

x = [values[0][0], values[1][0], values[2][0], values[3][0], values[0][0]]
y = [values[0][1], values[1][1], values[2][1], values[3][1], values[0][1]]

plt.plot(x, y,"ro-")
plt.grid()
plt.show()