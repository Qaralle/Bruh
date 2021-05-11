from services.function import empirical_draw, polygon_draw, histogram_draw, polygon_inter_draw
from services.variational import make_variational
import math


def start():
    n = int(input("Введите количество элементов в выборке: "))
    a = [float(input("Введите " + str(i + 1) + "-е число: ")) for i in range(n)]

    mapper = dict()
    prob = dict()

    for i in range(n):
        if mapper.get(a[i]) is None:
            mapper[a[i]] = 1
        else:
            mapper[a[i]] += 1

    for key in mapper:
        prob[key] = mapper[key] / n

    b = make_variational(a)
    print("Вариационный ряд: " + str(b))
    print("Экстремальные значения: " + str(b[0]) + " и " + str(b[len(b) - 1]))
    print("Размах: " + str(b[len(b) - 1] - b[0]))

    m = 0
    for key in prob:
        m += key * prob[key]

    print("Математическое ожидание M(x): ", str(m))

    d = 0
    for key in prob:
        d += ((key - m) ** 2) * prob[key]

    s = math.sqrt(d)

    print("Среднеквадратичное отклонение S: ", str(s))

    empirical_draw(prob)
    polygon_draw(prob)
    histogram_draw(a, b[len(b) - 1], b[0])
    polygon_inter_draw(a, b[len(b) - 1], b[0])
