from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QLineEdit

from convolutions.correlation import correlation
from convolutions.filter import filter_response
from gui.utils import layouting


class ConvolutionTab(QWidget):
    def __init__(self, plot, parent=None):
        super(ConvolutionTab, self).__init__(parent)
        self.plot = plot
        main_layout = QVBoxLayout(self)

        # filtering bottom rect
        self.textb_k1 = QLineEdit(self)
        self.textb_k1.setText('%d' % 8)
        self.textb_m1 = QLineEdit(self)
        self.textb_m1.setText('%d' % 7)
        self.textb_fs1 = QLineEdit(self)
        self.textb_fs1.setText('{:4.1f}'.format(1.0))
        self.chb_filtering1 = QCheckBox(self)

        # filtering f2 o2
        self.textb_k2 = QLineEdit(self)
        self.textb_k2.setText('%d' % 8)
        self.textb_m2 = QLineEdit(self)
        self.textb_m2.setText('%d' % 7)
        self.textb_fs2 = QLineEdit(self)
        self.textb_fs2.setText('{:4.1f}'.format(1.0))
        self.chb_filtering2 = QCheckBox(self)

        # correlation
        self.textb_delay = QLineEdit(self)
        self.textb_delay.setText('%d' % 20)
        self.chb_correlation = QCheckBox(self)
        self.chb_correlation_show = QCheckBox(self)

        # together
        layout = [[QLabel('Filtr dolnoprzepustowy'), self.chb_filtering1,
                   QLabel('K'), self.textb_k1, QLabel('M'), self.textb_m1, QLabel('fs'), self.textb_fs1],
                  [QLabel('Filtr górnoprzepustowy Hanning'), self.chb_filtering2,
                   QLabel('K'), self.textb_k2, QLabel('M'), self.textb_m2, QLabel('fs'), self.textb_fs2],
                  [QLabel('Korelacja'), self.chb_correlation,
                   QLabel('Opóźnienie w próbkach'), self.textb_delay,
                   QLabel('Pokaż korelacje'), self.chb_correlation_show]
                  ]
        self.setLayout(layouting(main_layout, layout))
        self.connect()

    def connect(self):
        # filtering bottom rect
        self.chb_filtering1.stateChanged.connect(self.update)
        self.textb_m1.returnPressed.connect(self.update)
        self.textb_k1.returnPressed.connect(self.update)
        self.textb_fs1.returnPressed.connect(self.update)
        # filtering f2 o2
        self.chb_filtering2.stateChanged.connect(self.update)
        self.textb_m2.returnPressed.connect(self.update)
        self.textb_k2.returnPressed.connect(self.update)
        self.textb_fs1.returnPressed.connect(self.update)
        # correlation
        self.chb_correlation.stateChanged.connect(self.update)
        self.textb_delay.returnPressed.connect(self.update)
        self.chb_correlation_show.stateChanged.connect(self.update)

    def update(self):
        extras = [None, None, None, None,
                  None, None]
        analog = (self.plot.alg1, self.plot.alg2, self.plot.merge_method)
        self.plot.show_main = True
        # filtering bottom rect
        if self.chb_filtering1.isChecked():
            print(float(self.textb_fs1.text()))
            x, y, h = filter_response(int(self.textb_m1.text()), int(self.textb_k1.text()),
                                      float(self.textb_fs1.text()),
                                      'f0', None, *analog)
            self.plot.vector_x = x
            extras[0] = [x, y, {
                'color': 'orange',
                'marker': 'o',
                'linestyle': '-',
                'markersize': 4
            }]
            # debug h(n)
            extras[1] = [x[:len(h)], h, {
                'color': 'yellow',
                'marker': 'o',
                'linestyle': '-',
                'markersize': 3
            }]
        if self.chb_filtering2.isChecked():
            x, y, h = filter_response(int(self.textb_m2.text()), int(self.textb_k2.text()),
                                      float(self.textb_fs2.text()),
                                      'f2', 'o2', *analog)
            self.plot.vector_x = x
            extras[2] = [x, y, {
                'color': 'blue',
                'marker': 'o',
                'linestyle': '-',
                'markersize': 4
            }]
            # debug h(n)
            extras[3] = [x[:len(h)], h, {
                'color': 'cyan',
                'marker': 'o',
                'linestyle': '-',
                'markersize': 3
            }]
        if self.chb_correlation.isChecked():
            self.plot.show_main = False
            x, y1, y2, corr_y = correlation(int(self.textb_delay.text()), *analog)
            if not self.chb_correlation_show.isChecked():
                # normal
                extras[4] = [x, y1, {
                    'color': 'red',
                    'marker': 'o',
                    'linestyle': '-',
                    'markersize': 4
                }]
                # delayed
                extras[5] = [x, y2, {
                    'color': 'magenta',
                    'marker': 'o',
                    'linestyle': '-',
                    'markersize': 3
                }]
            else:
                # correlation
                extras[4] = [x, corr_y[:len(x)], {
                    'color': 'black',
                    'marker': 'o',
                    'linestyle': '-',
                    'markersize': 3
                }]
        self.plot.set_extras(extras)
