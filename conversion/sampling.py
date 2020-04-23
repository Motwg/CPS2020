from algorithm import Algorithm


def _decorator(func):

    def function_wrapper(f, alg1, alg2, merge):
        assert isinstance(alg1, Algorithm)
        alg4 = None
        if alg2 is not None:
            assert isinstance(alg2, Algorithm)
            alg4 = alg2.__copy__()
        alg3 = alg1.__copy__()
        # change of frequency
        alg3.kwargs['f'] = f
        alg3.kwargs['d'] = alg1.kwargs['d'] - alg1.kwargs['f'] + f/2
        return func(alg3, alg4, merge)

    return function_wrapper


# Próbkowanie równomierne
@_decorator
def s1(alg1, alg2, merge):
    if merge is None or alg2 is None:
        return alg1.perform_algorithm()
    else:
        return merge(alg1, alg2)