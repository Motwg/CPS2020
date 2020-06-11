from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QComboBox, QLabel

from gui.utils import layouting
from transformation.sample_signals import signal_switcher


class TransformationTab(QWidget):
    def __init__(self, plot, parent=None):
        super(TransformationTab, self).__init__(parent)
        self.plot = plot
        main_layout = QVBoxLayout(self)

        # choose function
        self.chb_signal = QCheckBox(self)
        self.cb_signal = QComboBox(self)
        self.cb_signal.addItems(['S1', 'S2', 'S3'])

        # choose transformation and inverted transformation
        self.chb_transformation = QCheckBox(self)
        self.cb_transformation = QComboBox(self)
        self.cb_transformation.addItems(['F2', 'T3'])

        self.chb_i_transformation = QCheckBox(self)

        # together
        layout = [[QLabel('Sygnał zadaniowy'), self.chb_signal, self.cb_signal],
                  [QLabel('Transformacja '), self.cb_transformation, self.chb_transformation],
                  [QLabel('Odwrotna transformacja '), self.chb_i_transformation]]
        self.setLayout(layouting(main_layout, layout))
        self.connect()

    def connect(self):
        self.chb_signal.stateChanged.connect(self.update)
        self.cb_signal.currentIndexChanged.connect(self.update)
        self.chb_transformation.stateChanged.connect(self.update)
        self.chb_i_transformation.stateChanged.connect(self.update)
        self.cb_transformation.currentIndexChanged.connect(self.update)

    def update(self):
        extras = [None]
        extras_i = [None]
        if self.chb_signal.isChecked():
            self.plot.alg1.kwargs['f'] = 1 / 16
            self.plot.alg1.kwargs['function'] = signal_switcher(self.cb_signal.currentText())

        if self.chb_transformation.isChecked():
            analog = (self.plot.alg1, self.plot.alg2, self.plot.merge_method)
            extras[0] = (0, 0, {
                     'color': 'orange',
                     'marker': 'o',
                     'linestyle': ' ',
                     'markersize': 4
                 })
            if self.chb_i_transformation.isChecked():
                pass
        self.plot.set_extras(extras, extras_i)
