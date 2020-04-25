from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout

from conversion.quantization import quantization_switcher
from conversion.reconstruction import reconstruction_switcher
from conversion.sampling import s1


class ConversionTab(QWidget):
    def __init__(self, plot, parent=None):
        super(ConversionTab, self).__init__(parent)
        self.plot = plot
        main_layout = QVBoxLayout(self)

        # sampling
        self.sampling_f = 100
        self.chb_sampling = QtWidgets.QCheckBox(self)
        self.textb_sampling = QtWidgets.QLineEdit(self)
        self.textb_sampling.setText('{:.1f}'.format(self.sampling_f))
        # quantization
        self.quantization_steps = 8
        self.chb_quantization = QtWidgets.QCheckBox(self)
        self.cb_quantization = QtWidgets.QComboBox(self)
        self.cb_quantization.addItems(['Q2'])
        self.textb_quanztization = QtWidgets.QLineEdit(self)
        self.textb_quanztization.setText('%d' % self.quantization_steps)
        # reconstruction
        self.chb_reconstruction = QtWidgets.QCheckBox(self)
        self.cb_reconstruction = QtWidgets.QComboBox(self)
        self.cb_reconstruction.addItems(['R1', 'R2', 'R3'])

        layout = [[QLabel('Próbkowanie'), self.chb_sampling, QLabel('f'), self.textb_sampling],
                  [QLabel('Kwantyzacja'), self.chb_quantization, self.cb_quantization,
                   QLabel('Poziomy kwantyzacji'), self.textb_quanztization],
                  [QLabel('Rekonstrukcja'), self.chb_reconstruction, self.cb_reconstruction]]
        for y in layout:
            h_box = QHBoxLayout()
            for x in y:
                h_box.addWidget(x)
            h_box.addStretch(1)
            main_layout.addLayout(h_box)
        self.setLayout(main_layout)
        self.connect()

    def connect(self):
        self.chb_sampling.stateChanged.connect(self.update)
        self.chb_quantization.stateChanged.connect(self.update)
        self.chb_reconstruction.stateChanged.connect(self.update)
        self.textb_sampling.returnPressed.connect(self.update)

    def update(self):
        extras = [None, None, None]
        if self.chb_sampling.isChecked():
            x, y = s1(1 / float(self.textb_sampling.text()),
                      self.plot.alg1, self.plot.alg2, self.plot.merge_method)
            extras[0] = [x, y, {
                'color': 'orange',
                'marker': 'o',
                'linestyle': '-',
                'markersize': 2
            }]
        if self.chb_quantization.isChecked():
            x, y = quantization_switcher(self.cb_quantization.currentText()) \
                (float(self.textb_quanztization.text()), self.plot.alg1, self.plot.alg2, self.plot.merge_method)
            extras[1] = [x, y, {
                'color': 'blue',
                'marker': 'o',
                'linestyle': '-',
                'markersize': 1.5
            }]
        if self.chb_reconstruction.isChecked():
            x, y = reconstruction_switcher(self.cb_reconstruction.currentText()) \
                (self.plot.alg1, self.plot.alg2, self.plot.merge_method)
            extras[2] = [x, y, {
                'color': 'green',
                'linestyle': '-',
                'markersize': 1.5
            }]
        self.plot.set_extras(extras)
