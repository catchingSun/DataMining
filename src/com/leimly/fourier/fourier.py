import matplotlib.pyplot as plt
import math
import random
from sklearn import metrics


class Fourier:

    raw_data_path = ""

    def __init__(self, raw_data_path):
        self.raw_data_path = raw_data_path
        return

    def read_raw_data(self, path):
        raw_data = []
        f = open(path, "r")
        f.readline()
        for line in f:
            if line != "\n" and line != "\r\n":
                if line[-1] == "\n":
                    raw_data.append(int(line[:-1]))
                elif line[-2:] == "\r\n":
                    raw_data.append(int(line[:-2]))
        f.close()

        return raw_data

    def add_voice_for_raw_data(self, raw_data):
        add_voice_data = raw_data
        for i in range(0, len(raw_data)):
            add_voice_data[i] += random.randint(0, 9)
        return add_voice_data

    def plot_raw_data(self, raw_data, color, label, title):

        plt.plot(raw_data, color, label=label)
        plt.ylabel('Number of Blowfly Eggs')
        plt.title(title)
        plt.legend(loc="best")
        return

    def fourier(self, raw_data):
        length = len(raw_data)
        dft = list()
        fourier_coefficient = list()
        for k in range(0, length):
            temp = 0.0 + 0.0j
            for n in range(0, length):

                alpha = 2 * math.pi * k * n / length
                temp += raw_data[n] * (math.cos(alpha) - 1j * math.sin(alpha))
            fourier_coefficient.append(temp.real ** 2 + temp.imag ** 2)
            dft.append(temp)

        return dft, fourier_coefficient

    def inverse_fourier(self, data, title):
        length = len(data)
        raw = list()
        for n in range(0, length):
            temp = 0.0 + 0.0j
            for k in range(0, length):

                alpha = 2 * math.pi * k * n / length
                temp += data[k] * (math.cos(alpha) + 1j * math.sin(alpha)) / length
            raw.append(temp)
        self.plot_raw_data(raw, "blue", title, title)

        return raw

    def dft_data_compression(self, dft):
        dft_reserve = dft[0:len(dft)/2]
        # dft_reserve.extend(dft[-len(dft)/4:])
        self.inverse_fourier(dft_reserve, "Compressed Data")
        return dft_reserve

    def dft_data_filter(self, dft_raw, threshold_value):
        dft = dft_raw
        # print dft
        for i in range(0, len(dft)):
            if (dft[i].real ** 2 + dft[i].imag ** 2) < threshold_value:
                dft[i] = 0 + 0j

        indft = self.inverse_fourier(dft, "Filtered Data")
        # self.plot_raw_data(indft, "Filter Data")
        return indft

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

    fl = Fourier("../data/ch3 eggs.txt")
    raw_data = fl.read_raw_data(fl.raw_data_path)
    add_voice_data = fl.add_voice_for_raw_data(raw_data)
    fl.plot_raw_data(raw_data, "blue", "Raw Data", "Eggs Series")
    fl.plot_raw_data(add_voice_data, "red", "Add Voice Data", "Eggs Series")
    plt.show()

    dft_raw, fourier_coefficient = fl.fourier(add_voice_data)
    print min(fourier_coefficient)
    fl.plot_raw_data(fourier_coefficient, "blue", "Fourier Coefficient", "Fourier Coefficient")
    plt.show()
    indft = fl.inverse_fourier(dft_raw, "Inverse DFT Data")
    fl.plot_raw_data(add_voice_data, "red", "Raw Data", "Eggs Series")
    plt.show()

    fl.dft_data_compression(dft_raw)
    plt.show()
    fl.dft_data_filter(dft_raw, 20000000)
    fl.plot_raw_data(add_voice_data, "red", "Raw Data", "Eggs Series")
    plt.show()
    # dft = fl.inverse_fourier(dft_raw)
    # dft_raw = fl.fourier(dft)
