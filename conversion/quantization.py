from algorithm import Algorithm


def quantization_switcher(quantization_code):
    switcher = {
        'q2': q2
    }
    return switcher.get(quantization_code.lower(), q2)


def _decorator(func):

    def function_wrapper(alg1, alg2, merge):
        assert isinstance(alg1, Algorithm)
        alg4 = None
        if alg2 is not None:
            assert isinstance(alg2, Algorithm)
            alg4 = alg2.__copy__()
        alg3 = alg1.__copy__()
        return func(alg3, alg4, merge)

    return function_wrapper


# Kwantyzacja z zaokrągleniem
@_decorator
def q2(alg1, alg2, merge):
    if merge is None or alg2 is None:
        vector_x, vector_y = alg1.perform_algorithm()
    else:
        vector_x, vector_y = merge(alg1, alg2)

    new_x, new_y = [], []
    for i, (x, y) in enumerate(zip(vector_x, vector_y)):
        new_x.append(x)
        new_y.append(y)
        if i % 2 == 1 and i < len(vector_x) - 1:
            new_x.append(vector_x[i + 1])
            new_y.append(y)
        elif i < len(vector_x) - 1:
            new_x.append(x)
            new_y.append(vector_y[i + 1])
    return new_x, new_y
