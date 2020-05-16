from math import cos, pi


def window_switcher(window_code):
    switcher = {
        'o2': hanning_window
    }
    return switcher.get(window_code.lower(), hanning_window)


# okno Hanninga wzór 6
def hanning_window(n, M):
    return 0.5 - 0.5 * cos((2 * pi * n) / M)
