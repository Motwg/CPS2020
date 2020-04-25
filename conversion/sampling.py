from algorithm import Algorithm


def _decorator(func):

    def function_wrapper(f, alg1, alg2, merge):
        assert isinstance(alg1, Algorithm)
        if alg2 is not None and merge is not None:
            assert isinstance(alg2, Algorithm)
            vector_x, vector_y = merge(alg1, alg2)
        else:
            vector_x, vector_y = alg1.perform_algorithm()
        return func(f, vector_x, vector_y)
    return function_wrapper


# Próbkowanie równomierne
@_decorator
def s1(f, vector_x, vector_y):
    new_vx, new_vy = [], []
    sampled_x = vector_x[0]
    for i, (x, y) in enumerate(zip(vector_x, vector_y)):
        while round(sampled_x, 5) < round(x, 5):
            new_vx.append(sampled_x)
            new_vy.append(vector_y[i - 1])
            sampled_x += f
        else:
            if round(sampled_x, 5) == round(x, 5):
                new_vx.append(sampled_x)
                new_vy.append(y)
                sampled_x += f

    return new_vx, new_vy
