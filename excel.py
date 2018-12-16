import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

file_name = input("Type in the name of the file: ")
feature1 = int(input("Type feature 1: "))
feature2 = int(input("Type feature 2: "))

arr_data = []
classi = []
f1 = []
f2 = []

with open(file_name) as data_set:
    for line in data_set:
        arr = line.split()
        arr_tmp = []
        for num in arr:
            arr_tmp.append(float(num))
        arr_data.append(arr_tmp)

for i in range(len(arr_data)):
    classi.append(arr_data[i][0])

for i in range(1, len(arr_data[0])):
    if i == feature1:
        for j in range(len(arr_data)):
            f1.append(arr_data[j][i])
    elif i == feature2:
        for j in range(len(arr_data)):
            f2.append(arr_data[j][i])

data = []
for i in range(len(classi)):
    data.append([classi[i], f1[i], f2[i]])

print(len(data))

fig = plt.figure()

for instance in data:
    x = instance[1]
    y = instance[2]
    if instance[0] == 1.0:
        color = "red"
        group = 1.0
    elif instance[0] == 2.0:
        color = "blue"
        group = 2.0
    else:
        print('fail')
        break
    plt.scatter(x, y, alpha=0.8, c=color, edgecolors='none')

plt.title(str(feature1) + ' VS ' + str(feature2))
plt.show()
