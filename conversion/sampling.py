from core.merging import perform_merge


def _decorator(func):

    def function_wrapper(f, alg1, alg2, merge):
        analog_x, analog_y = perform_merge(alg1, alg2, merge)
        return func(f, analog_x, analog_y)
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
