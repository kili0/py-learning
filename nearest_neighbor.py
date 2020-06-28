import matplotlib.pyplot as plt
import numpy as np

SIZE = 1000*1000

class DATA:
    def __init__(self):
        self.x = 0
        self.y = 0
        
data = [0] * SIZE
        
for i in range(SIZE):
    data[i] = DATA()
    data[i].x = np.random.randint(0, 10000)
    data[i].y = np.random.randint(0, 10000)

print("xy?\n")
key = DATA()
key.x, key.y = (int(p) for p in input().split())

minkey = -1
min = float(1000*1000)

for i in range(SIZE):
    distance = (data[i].x - key.x)**2 + (data[i].y - key.y)**2
    if (distance < min):
        min = distance
        minkey = i
        
print("key: " + str(minkey))
print("value: " + str(distance))

fig = plt.figure(figsize = (15.0, 15.0))
ax = fig.add_subplot(111)

plt.xlabel = "x"
plt.ylabel = "y"

data_x = [0] * SIZE
data_y = [0] * SIZE
for i in range(SIZE):
    data_x[i] = data[i].x
    data_y[i] = data[i].y

plt.scatter(data_x, data_y, c="b", s=3)    
plt.scatter(key.x, key.y, c="r")

plt.show()
