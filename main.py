import numpy as np
import pandas as pd

class som:
    def __init__(self, alpha,r,beta,et):
        self.alpha =alpha
        self.r = r
        self.beta = beta
        self.et = et
        # self.epoch = 1
        # self.w = [[0.3, 0.9, 0.7, 0.2],
        #           [0.1,0.5,0.8,0.4],
        #           [0.9,0.7,0.3,0.4],
        #           [0.1,0.5,0.8,0.3]]

        self.w = [[0.2, 0.6, 0.5, 0.9],
                  [0.8,0.4,0.7,0.3]]

        # self.w = np.random.rand(2,23)

    def readcsv(self, filename):
        self.data = pd.read_csv(filename)
        return (np.array(self.data))

    def neuronPemenang(self,data):
        temp = [0]*len(data)
        temps = [0]*len(self.w)
        for i in range(len(data)):
            temp2 = [0]*len(self.w)
            for j in range(len(self.w)):
                for k in range(len(self.w[j])):
                    temp2[j] += pow(np.subtract(self.w[j][k] , data[i][k]), 2)
                index = np.argmin(temp2)
                temp[i]= index #index neuron pemenang
        return temp

    def TuningPhase(self, data, index): #update bobot neuron pemenenag
        temps = [0] * len(data)
        j = 0
        for i in range(len(data)):
            for j in range(j, j+len(index)):
                temp = index[j]
                self.w[temp] = np.add(self.w[temp], self.alpha * np.array((np.subtract(data[i], self.w[temp]))))
                break
            j+=1
            temps[i] = self.w[temp]
        return temps

    def OrderingPhase(self, data, index): #update bobot neuron pemenang dan tetangga
        return

    def updateBobot(self):
        data = self.readcsv('coba.csv')
        index = self.neuronPemenang(data)
        if self.r == 0:
            bobot = self.TuningPhase(data, index)
        elif self.r>0:
            bobot= self.OrderingPhase(data,index)
        else:
            print("error")
        return bobot


    def berhenti(self):
        data = self.readcsv('coba.csv')
        index = self.neuronPemenang(data)
        epoch = 1
        for i in range(self.et):
            if epoch <= self.et:
                b = self.neuronPemenang(data)
                a = self.updateBobot()
                print('epoch', epoch, ': \n', 'neuron pemenang :', b, '\n update bobot: \n',a)
                epoch += 1
                self.alpha *= self.beta
                print("alpha: ",self.alpha)
        return ""
