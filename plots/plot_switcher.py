def plot_switcher(plot_code):
    switcher = {
        'w0': real_hist,
        'w1': real_imag,
        'w2': mod_arg,
        'w3': polar
    }
    return switcher.get(plot_code.lower(), 'w0')


def real_hist(fig, v_x, v_y, bins, show_main=True, **kwargs):
    real = fig.add_subplot(121)
    hist = fig.add_subplot(122)

    if show_main:
        real.plot(v_x, v_y, linestyle='-', marker='o', color='red', markersize=1.4)
    real.grid(True)
    real.margins(0.01, 0.05)
    real.set_xlabel('t[s]')

    hist.hist(v_y, bins=bins)
    hist.grid(True)
    if kwargs['extras'] is not None:
        draw_extras(real, kwargs['extras'])


def real_imag(fig, v_x, v_y, v_i, show_main=True, **kwargs):
    real = fig.add_subplot(211)
    imag = fig.add_subplot(212)

    if show_main:
        real.plot(range(len(v_y)), v_y, linestyle='-', marker='o', color='red', markersize=1.4)
        imag.plot(range(len(v_i)), v_i, linestyle='-', marker='o', color='red', markersize=1.4)
    real.grid(True)
    real.margins(0.01, 0.05)
    real.set_ylabel('real')
    real.set_xlabel('f[Hz]')

    imag.grid(True)
    imag.margins(0.01, 0.05)
    imag.set_ylabel('imag')
    imag.set_xlabel('f[Hz]')

    if kwargs['extras'] is not None:
        draw_extras(real, kwargs['extras'], x_given=False)
    if kwargs['extras_i'] is not None:
        draw_extras(imag, kwargs['extras_i'], x_given=False)


def mod_arg(fig, v_y, v_i, show_main=True, **kwargs):
    mod = fig.add_subplot(211)
    arg = fig.add_subplot(212)

    if show_main:
        mod.plot(range(len(v_y)), v_y, linestyle='-', marker='o', color='red', markersize=1.4)
        arg.plot(range(len(v_i)), v_i, linestyle='-', marker='o', color='red', markersize=1.4)
    mod.grid(True)
    mod.margins(0.01, 0.05)
    mod.set_xlabel('f[Hz]')
    mod.set_ylabel('|Z|')

    arg.grid(True)
    arg.margins(0.01, 0.05)
    arg.set_xlabel('f[Hz]')
    arg.set_ylabel('arg')

    if kwargs['extras'] is not None:
        draw_extras(mod, kwargs['extras'], x_given=False)
    if kwargs['extras_i'] is not None:
        draw_extras(arg, kwargs['extras_i'], x_given=False)


def polar(fig, **kwargs):
    pol = fig.add_subplot(111)
    pol.grid(True)

    try:
        extras = kwargs['extras']
        extras_i = kwargs['extras_i']
        print([(extras[0][1], extras_i[0][1], extras[0][2])])
        draw_extras(pol, [(extras[0][1], extras_i[0][1], extras[0][2])], x_given=True)
    except Exception:
        pass


def draw_extras(ax, extras, x_given=True):
    for extra in extras:
        if extra is not None:
            if x_given:
                ax.plot(extra[0], extra[1], **extra[2])
            else:
                ax.plot(range(len(extra[1])), extra[1], **extra[2])
