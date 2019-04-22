import numpy as np
import pandas as pd

r = 0
alpha = 0.6
beta = 0.5
w = [[0.2, 0.6, 0.5, 0.9],
     [0.8,0.4,0.7,0.3]]

def readcsv(filename):
    data = pd.read_csv(filename)
    return (np.array(data))

def neuronPemenang(data):
    temp = [0]*len(data)
    for i in range(len(data)):
        temp2 = np.zeros((len(w)))
        for j in range(len(w)):
            for k in range(len(w[j])):
                temp2[j] += pow(np.subtract(w[j][k] , data[i][k]), 2)
            index = np.argmin(temp2)
            temp[i]= index #index neuron pemenang
    return temp

# def R():
#     if R == 0:
#         updateBobot()
#     else:

def updateBobot(data, index):
    temps = [0] * len(data)
    j = 0
    for i in range(len(data)):
        for j in range(j, j+4):
            temp = index[j]
            if r == 0:
                w[temp] = np.add(w[temp], alpha * np.array((np.subtract(data[i], w[temp]))))
            # break
            else:
                w[temp] = np.add(w[temp], alpha * np.array((np.subtract(data[i], w[temp]))))
        j+=1
        temps[i] = w[temp]
    return temps

array = readcsv('coba.csv')
index = neuronPemenang(array)
print("array\n",array)
print("neuron pemenang\n",index)
print("update bobot \n", updateBobot(array,index))










