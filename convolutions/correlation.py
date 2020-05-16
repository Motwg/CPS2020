from convolutions.convolution import convolution
from core.algorithm import Algorithm
from core.merging import perform_merge


def _decorator(func):
    def function_wrapper(delay, alg1, alg2, merge):
        assert isinstance(alg1, Algorithm)
        alg1c = alg1.__copy__()
        alg1c.kwargs['d'] = alg1c.kwargs['d'] + delay
        analog_x, analog_y = perform_merge(alg1c, alg2, merge)
        correlation_y = func(analog_y, delay)
        return analog_x[:-delay], analog_y[:-delay], analog_y[delay:], correlation_y

    return function_wrapper


@_decorator
def correlation(analog_y, delay):
    return convolution(analog_y[:-delay], analog_y[delay:])
