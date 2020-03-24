from math import fabs, sqrt


def mean(vector_x, vector_y):
    if len(vector_y) > 0:
        return sum(vector_y) / len(vector_y)
    else:
        return 0


def absmean(vector_x, vector_y):
    if len(vector_y) > 0:
        return sum(map(fabs, vector_y)) / len(vector_y)
    else:
        return 0


def ms(vector_x, vector_y):
    if len(vector_y) > 0:
        value = 0
        for y in vector_y:
            value += y * y
        return value / len(vector_y)
    else:
        return 0


def war(vector_x, vector_y):
    if len(vector_y) > 0:
        value = 0
        for y in vector_y:
            value += (y - mean(vector_x, vector_y)) ** 2
        return value / len(vector_y)
    else:
        return 0


def ws(vector_x, vector_y):
    return sqrt(ms(vector_x, vector_y))