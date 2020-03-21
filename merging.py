from Algorithm import Algorithm


def _decorator(func):
    def function_wrapper(alg1, alg2):
        assert isinstance(alg1, Algorithm)
        assert isinstance(alg2, Algorithm)

        # takes t1, d and f parameters from first function
        for kwarg in ['t1', 'd', 'f']:
            alg2.kwargs[kwarg] = alg1.kwargs[kwarg]
        return func(alg1, alg2)

    return function_wrapper


@_decorator
def add(alg1, alg2):
    vector_x, vector_y1 = alg1.perform_algorithm()
    _, vector_y2 = alg2.perform_algorithm()
    assert len(vector_y1) == len(vector_y2)
    return vector_x, [y1 + y2 for y1, y2 in zip(vector_y1, vector_y2)]


@_decorator
def add(alg1, alg2):
    vector_x, vector_y1 = alg1.perform_algorithm()
    _, vector_y2 = alg2.perform_algorithm()
    assert len(vector_y1) == len(vector_y2)
    return vector_x, [y1 + y2 for y1, y2 in zip(vector_y1, vector_y2)]


@_decorator
def subtract(alg1, alg2):
    vector_x, vector_y1 = alg1.perform_algorithm()
    _, vector_y2 = alg2.perform_algorithm()
    assert len(vector_y1) == len(vector_y2)
    return vector_x, [y1 - y2 for y1, y2 in zip(vector_y1, vector_y2)]


@_decorator
def multiply(alg1, alg2):
    vector_x, vector_y1 = alg1.perform_algorithm()
    _, vector_y2 = alg2.perform_algorithm()
    assert len(vector_y1) == len(vector_y2)
    return vector_x, [y1 * y2 for y1, y2 in zip(vector_y1, vector_y2)]


@_decorator
def divide(alg1, alg2):
    vector_x, vector_y1 = alg1.perform_algorithm()
    _, vector_y2 = alg2.perform_algorithm()
    assert len(vector_y1) == len(vector_y2)
    vector_y = []
    for y1, y2 in zip(vector_y1, vector_y2):
        if y2 != 0:
            vector_y.append(y1 / y2)
        else:
            vector_y.append(None)
    return vector_x, vector_y
