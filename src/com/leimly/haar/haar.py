import matplotlib.pyplot as plt
import math as m
import random
from sklearn import metrics


class Haar:

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

    def plot_data(self, data, color, label, title):

        plt.plot(data, color, label=label)
        # plt.xlabel('Time')
        plt.ylabel('Number of Blowfly Eggs')
        plt.title(title)
        plt.legend(loc="best")
        return

    def haar(self, layer, raw_data):
        i = 1
        length = len(raw_data)
        low_frequency = raw_data
        while i <= layer:
            high_frequency = []
            temp = list()
            # print length
            # print length / (2 ** i) - 1
            for j in range(0, length / (2 ** i)):
                a = (low_frequency[2 * j] + low_frequency[2 * j + 1]) / m.sqrt(2)
                d = (low_frequency[2 * j] - low_frequency[2 * j + 1]) / m.sqrt(2)
                high_frequency.append(d)
                temp.append(a)
            low_frequency = temp
            i += 1
            # self.plot_data(low_frequency)
        # self.plot_raw_data(tempD)
        return low_frequency, high_frequency

    def smooth_high_frequency(self, threshold_value, high_frequency):

        high_frequency_smoothed = high_frequency
        for i in range(0, len(high_frequency_smoothed)):
            if high_frequency_smoothed[i] < threshold_value:
                high_frequency_smoothed[i] = 0

        return high_frequency_smoothed

    def inverse_haar(self, low_frequency, high_frequency_smoothed):
        signal_smoothed = list()
        for i in range(0, len(low_frequency)):
            temp1 = (low_frequency[i] + high_frequency_smoothed[i]) / m.sqrt(2)
            temp2 = (low_frequency[i] - high_frequency_smoothed[i]) / m.sqrt(2)
            signal_smoothed.append(temp1)
            signal_smoothed.append(temp2)
        return signal_smoothed

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

    fl = Haar("../data/ch3 eggs.txt")
    raw_data = fl.read_raw_data(fl.raw_data_path)
    threshold_value = 5
    # fl.plot_data(raw_data, "Raw Data")
    low_frequency, high_frequency = fl.haar(1, raw_data)
    inverse_data = fl.inverse_haar(low_frequency, high_frequency)
    # fl.plot_data(raw_data, "blue","Raw Data", "Eggs Series")
    # fl.plot_data(inverse_data,"red", "Inverse DWT Data", "Eggs Series")
    # plt.show()
    # fl.plot_data(low_frequency, "The Low-frequency Coefficient")
    # fl.plot_data(high_frequency, "The High-frequency Coefficient")
    high_frequency_smoothed = fl.smooth_high_frequency(threshold_value, high_frequency)

    # fl.plot_data(high_frequency_smoothed, "Threshold Quantization the High-frequency Coefficient")

    signal_smoothed = fl.inverse_haar(low_frequency, high_frequency_smoothed)
    # fl.plot_data(raw_data, "blue","Raw Data", "Eggs Series")
    # fl.plot_data(signal_smoothed,"red", "Filtered Data", "Eggs Series")
    #
    # plt.show()

