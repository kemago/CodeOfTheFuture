# importáljuk a szükséges modult
import matplotlib.pyplot as plt

# PLotting Graphs is Python
# Egyszerű diagram
x = [1, 3, 5, 10]
plt.plot(x)
plt.show()

# Diagram - két adatsor alapján
y = [7, 12, 21, 22]
plt.plot(x, y)
plt.show()

# Egy érdekes diagram
# Első adatsor pontjai
x = [3, 9, 14]
y = [2, 7, 30]
plt.plot(x, y, c='red', linewidth=2, label='Line 1')
#plt.show()

# Második adatsor pontjai
x2 = [1, 15, 18]
y2 = [0, 3, 12]
plt.plot(x2, y2, c='green', linewidth=0.5, label='Line 2', linestyle='dashed',
         marker='o', markerfacecolor='orange', markersize=10)
# plt.show()

# Label the axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Two lines!')

#Limits of the axes
plt.ylim(1, 10)
plt.xlim(0, 30)

#Show the legend on the plot
plt.legend()
#Get Python to show the plot
plt.show()