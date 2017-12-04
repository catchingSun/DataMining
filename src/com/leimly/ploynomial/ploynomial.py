import matplotlib.pyplot as plt
from sklearn import metrics
import numpy as np


class Ploynomial:

    def __init__(self):

        return

    def read_raw_data(self, path):
        raw_data = []
        f = open(path, "r")
        # print f.readline()

        for line in f:
            if line != "\n" and line != "\r\n":

                if line[-1] == "\n" and line[-2:] != "\r\n":
                    if line.__contains__("["):
                        raw_data.extend(line[:-1].split("[")[1].split(",")[:-1])
                    elif line.__contains__("]"):
                        raw_data.extend(line[:-1].split("]")[0].split(","))
                    else:
                        raw_data.extend(line[:-1].split(",")[:-1])

                elif line[-2:] == "\r\n":
                    if line.__contains__("["):
                        raw_data.extend(line[:-2].split("[")[1].split(",")[:-1])
                    elif line.__contains__("]"):
                        raw_data.extend(line[:-2].split("]")[0].split(","))
                    else:
                        raw_data.extend(line[:-2].split(",")[:-1])
        f.close()

        # raw_data = [float(i) for i in raw_data: for j in i]
        raw_data = map(float, raw_data)
        length = len(raw_data)
        raw_data = np.matrix(raw_data).T
        # self.plot_data(raw_data, 'huaxuefanying series')
        return raw_data, length

    def plot_data(self, raw_data, ploynomial_data, title):

        plt.plot(raw_data, '.', label='Raw Data')
        plt.plot(ploynomial_data, label='Fitted Data')
        plt.ylabel('huaxuefanying')
        plt.legend()
        # plt.legend('Fitted Data')
        plt.title(title)
        plt.show()
        return

    def ploynomial(self, p, raw_data, length):
        x = list()
        for i in range(1, length + 1):
            temp = list()
            for j in range(0, p + 1):
               temp.append(i ** j)
            # print temp
            x.append(temp)
        x = np.matrix(x)
        # print x
        w = (x.T * x).I * x.T * raw_data
        result = x * w
        # print len(result)
        # self.plot_data(result, "dddd")
        # print w
        pl.plot_data(raw_data, result, "Huaxuefanying Raw Data Series and Fitted Data Series(p = " + str(p) + ")")
        pl.calculate_mse(raw_data, result, p, "../data/ch3 huaxuefy_mse.txt", w.T)
        return result

    def calculate_mse(self, raw_data, ploynomial_data, p, mse_path, w):
        mse = metrics.mean_squared_error(raw_data, ploynomial_data)
        data = "p = " + str(p) + " , mse = " + str(mse) + " , w = " + str(w)
        path = mse_path
        mse_file = open(path, 'a+')
        mse_file.write(str(data))
        mse_file.write("\n")
        mse_file.close()
        return


if __name__ == '__main__':
    pl = Ploynomial()
    for p in range(0, 6):
        raw_data, length = pl.read_raw_data("../data/ch3 huaxuefy.m")
        result = pl.ploynomial(p, raw_data, length)
        # pl.plot_data(raw_data, result, "Huaxuefanying Raw Data Series and Fitted Data Series")
        # pl.calculate_mse(raw_data, result, p, "../data/ch3 huaxuefy_mse.txt")