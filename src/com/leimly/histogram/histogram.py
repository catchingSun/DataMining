import matplotlib.pyplot as plt


class Histogram:

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
        raw_data.sort(reverse=False)
        return raw_data

    def plot_data(self, raw_data):

        plt.plot(raw_data)
        plt.xlabel('Time')
        plt.ylabel('Number of Blowfly Eggs')
        plt.title('Raw Blowfly Eggs Series')
        plt.show()
        return

    def width_histogram(self, raw_data):
        width = max(raw_data) / len(raw_data)
        print range(0, width + 2)
        width_histogram = [0 for i in range(width + 2)]

        for i in raw_data:
            if i / width < len(raw_data):
                # print i / width
                width_histogram[i / width] += 1
        # print width_histogram
        return

    def depth_histogram(self, raw_data):

        return


if __name__ == '__main__':

    fl = Histogram("../data/ch3 eggs.txt")
    raw_data = fl.read_raw_data(fl.raw_data_path)
    fl.width_histogram(raw_data)
    # fl.plot_data(raw_data)