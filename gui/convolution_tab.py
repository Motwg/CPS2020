from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QLineEdit

from convolutions.filter import filter_response
from gui.conversion_tab import layouting


class ConvolutionTab(QWidget):
    def __init__(self, plot, parent=None):
        super(ConvolutionTab, self).__init__(parent)
        self.plot = plot
        main_layout = QVBoxLayout(self)

        # filtering
        self.filtering_k = 8
        self.textb_k = QLineEdit(self)
        self.textb_k.setText('%d' % self.filtering_k)
        self.filtering_m = 7
        self.textb_m = QLineEdit(self)
        self.textb_m.setText('%d' % self.filtering_m)
        self.chb_filtering = QCheckBox(self)

        # together
        layout = [[QLabel('Filtr'), self.chb_filtering, QLabel('K'), self.textb_k, QLabel('M'), self.textb_m]]
        self.setLayout(layouting(main_layout, layout))
        self.connect()

    def connect(self):
        self.chb_filtering.stateChanged.connect(self.update)
        self.textb_m.returnPressed.connect(self.update)
        self.textb_k.returnPressed.connect(self.update)

    def update(self):
        extras = [None, None]
        analog = (self.plot.alg1, self.plot.alg2, self.plot.merge_method)
        # filtering
        if self.chb_filtering.isChecked():
            x, y, h = filter_response(int(self.textb_m.text()), int(self.textb_k.text()), *analog)
            self.plot.vector_x = x
            extras[0] = [x, y, {
                'color': 'orange',
                'marker': 'o',
                'linestyle': '-',
                'markersize': 4
            }]
            extras[1] = [x[:len(h)], h, {
                'color': 'green',
                'marker': 'o',
                'linestyle': '-',
                'markersize': 3
            }]
        self.plot.set_extras(extras)
