import math

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import  numpy as np

label_format = '{:.2f}'


def prepare_function(prob, x):
    answer = 0
    keys = sorted(prob)
    for key in keys:
        if key <= x:
            answer += prob[key]
        else:
            break
    return answer


def empirical_draw(prob):
    t = [float(key) for key in prob]
    t = sorted(t)
    x = [i for i in np.arange(int(t[0] - 0.5), (int(t[len(t) - 1]) + 1), 0.0001)]

    y = [prepare_function(prob, x) for x in x]

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.grid()

    fig.savefig("test.png")
    plt.show()


def polygon_draw(prob):
    t = [key for key in prob]
    t = sorted(t)

    y = [prob[x] for x in t]

    fig, ax = plt.subplots()
    ax.plot(t, y)

    ax.grid()

    fig.savefig("test2.png")
    plt.show()


def __prepare_bins(x, max, min):
    kostyl = math.log2(len(x)) + 1
    n = int(math.ceil(kostyl))

    h = (max - min) / kostyl

    start = min - h / 2

    intr = [start + i * h for i in range(0, n + 1)]

    return intr, h


def histogram_draw(x, max, min):
    fig, ax = plt.subplots()

    intr, h = __prepare_bins(x, max, min)

    # ni/h
    ax.hist(x, bins=intr)

    ns = ax.get_yticks()
    ax.yaxis.set_major_locator(mticker.FixedLocator(ns))
    ax.set_yticklabels([label_format.format(ni / h) for ni in ns])
    ax.grid()

    fig.savefig("test3.png")
    plt.show()


def polygon_inter_draw(x, max, min):
    fig, ax = plt.subplots()
    intr, _ = __prepare_bins(x, max, min)

    freqs = []
    for i in range(len(intr)):
        if i != 0:
            freqs.append(0)
            for xi in x:
                if intr[i - 1] <= xi < intr[i]:
                    freqs[i - 1] += 1
    x_arr = []

    for i in range(len(freqs)):
        freqs[i] /= len(x)
        x_arr.append((intr[i + 1] + intr[i]) / 2)

    ax.plot(x_arr, freqs)
    fig.savefig("test4.png")
    plt.show()
