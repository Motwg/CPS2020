from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QLineEdit

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
        self.chb_filtering1 = QCheckBox(self)

        # filtering second
        self.textb_k2 = QLineEdit(self)
        self.textb_k2.setText('%d' % 8)
        self.textb_m2 = QLineEdit(self)
        self.textb_m2.setText('%d' % 7)
        self.chb_filtering2 = QCheckBox(self)

        # together
        layout = [[QLabel('Filtr dolnoprzepustowy'), self.chb_filtering1,
                   QLabel('K'), self.textb_k1, QLabel('M'), self.textb_m1],
                  [QLabel('Filtr drugi'), self.chb_filtering2,
                   QLabel('K'), self.textb_k2, QLabel('M'), self.textb_m2]]
        self.setLayout(layouting(main_layout, layout))
        self.connect()

    def connect(self):
        # filtering bottom rect
        self.chb_filtering1.stateChanged.connect(self.update)
        self.textb_m1.returnPressed.connect(self.update)
        self.textb_k1.returnPressed.connect(self.update)
        # filtering second
        self.chb_filtering2.stateChanged.connect(self.update)
        self.textb_m2.returnPressed.connect(self.update)
        self.textb_k2.returnPressed.connect(self.update)

    def update(self):
        extras = [None, None, None]
        analog = (self.plot.alg1, self.plot.alg2, self.plot.merge_method)
        # filtering bottom rect
        if self.chb_filtering1.isChecked():
            x, y, h = filter_response(int(self.textb_m1.text()), int(self.textb_k1.text()), *analog)
            self.plot.vector_x = x
            extras[0] = [x, y, {
                'color': 'orange',
                'marker': 'o',
                'linestyle': '-',
                'markersize': 4
            }]
            # debug h(n)
            extras[1] = [x[:len(h)], h, {
                'color': 'green',
                'marker': 'o',
                'linestyle': '-',
                'markersize': 3
            }]
        if self.chb_filtering2.isChecked():
            # todo change to new proper function
            x, y, h = filter_response(int(self.textb_m1.text()), int(self.textb_k1.text()), *analog)
            self.plot.vector_x = x
            extras[2] = [x, y, {
                'color': 'blue',
                'marker': 'o',
                'linestyle': '-',
                'markersize': 4
            }]
        self.plot.set_extras(extras)
