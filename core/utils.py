def multiply_vectors(v1, v2):
    if len(v2) > len(v1):
        v1, v2 = v2, v1
    return [x * y for x, y in zip(v1, v2)] + v1[len(v2):]


def add_vectors(v1, v2):
    if len(v2) > len(v1):
        v1, v2 = v2, v1
    return [x + y for x, y in zip(v1, v2)] + v1[len(v2):]


def extend(v, length):
    while len(v) < length:
        v.append(v[-1] + v[1] - v[0])
    return v
