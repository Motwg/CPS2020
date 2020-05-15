import math
from random import uniform, gauss, choices


def function_switcher(function_code):
    switcher = {
        's1': s1_noise,
        's2': s2_gauss,
        's3': s3_sin,
        's4': s4_sin_one_side,
        's5': s5_sin_two_side,
        's6': s6_rectangle,
        's7': s7_rectangle_symmetrical,
        's8': s8_triangle,
        's9': s9_unit_j,
        's10': s10_unit_imp,
        's11': s11_noise_imp
    }
    return switcher.get(function_code, s12)


# Szum o rozkładzie jednostajnym
def s1_noise(t, **kwargs):
    return uniform(-kwargs['A'], kwargs['A'])


# Szum gaussa
def s2_gauss(t, **kwargs):
    return kwargs['A'] * gauss(0, 1)


# Sygnał sinusoidalny
def s3_sin(t, **kwargs):
    return kwargs['A'] * math.sin(math.pi * 2 / kwargs['T'] * (t - kwargs['t1']))


# Sygnał sinusoidalny wyprostowany jednopołówkowo
def s4_sin_one_side(t, **kwargs):
    return kwargs['A'] / 2 * (
            math.sin(math.pi * 2 / kwargs['T'] * (t - kwargs['t1']))
            + math.fabs(
        math.sin(math.pi * 2 / kwargs['T'] * (t - kwargs['t1']))
    )
    )


# Sygnał sinusoidalny wyprostowany dwupołówkowo
def s5_sin_two_side(t, **kwargs):
    return math.fabs(kwargs['A'] * math.sin(math.pi * 2 / kwargs['T'] * (t - kwargs['t1'])))


# Sygnał prostokątny
def s6_rectangle(t, **kwargs):
    k = (t - kwargs['t1']) // kwargs['T']
    if k * kwargs['T'] + kwargs['t1'] <= t < kwargs['kw'] * kwargs['T'] + k * kwargs['T'] + kwargs['t1']:
        return kwargs['A']
    else:
        return 0


# Sygnał prostokątny symetryczny
def s7_rectangle_symmetrical(t, **kwargs):
    if s6_rectangle(t, **kwargs) == 0:
        return -kwargs['A']
    else:
        return kwargs['A']


# Sygnał trójkątny/piłokształtny
def s8_triangle(t, **kwargs):
    k = (t - kwargs['t1']) // kwargs['T']
    if k * kwargs['T'] + kwargs['t1'] <= t < kwargs['kw'] * kwargs['T'] + k * kwargs['T'] + kwargs['t1']:
        return kwargs['A'] / kwargs['T'] / kwargs['kw'] * (t - k * kwargs['T'] - kwargs['t1'])
    else:
        return -kwargs['A'] / kwargs['T'] / (1 - kwargs['kw']) * (t - k * kwargs['T'] - kwargs['t1']) \
               + kwargs['A'] / (1 - kwargs['kw'])


#  Skok jednostkowy
def s9_unit_j(t, **kwargs):
    if t > kwargs['ts']:
        return kwargs['A']
    elif t == kwargs['ts']:
        return kwargs['A'] / 2
    else:
        return 0


# Impuls jednostkowy
def s10_unit_imp(t, **kwargs):
    if round((t - kwargs['t1']) / kwargs['f'], 0) == round(kwargs['ns'], 0):
        return kwargs['A']
    else:
        return 0


# Szum impulsowy
def s11_noise_imp(t, **kwargs):
    if choices([True, False], [kwargs['p'], 1 - kwargs['p']])[0]:
        return kwargs['A']
    else:
        return 0


def s12(t, **kwargs):
    return t
