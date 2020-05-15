from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from conversion.quantization import quantization_switcher
from conversion.reconstruction import reconstruction_switcher
from conversion.sampling import s1
from conversion.similarity import similarity_switcher
from gui.utils import layouting


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
        # reconstruction
        self.chb_reconstruction = QtWidgets.QCheckBox(self)
        self.cb_reconstruction = QtWidgets.QComboBox(self)
        self.cb_reconstruction.addItems(['R1', 'R2', 'R3'])
        # info <= sampling + reconstruction
        sr_layout = QVBoxLayout()
        self.sr_label_mse = QLabel()
        self.sr_label_snr = QLabel()
        self.sr_label_md = QLabel()
        layout = [[QLabel('MSE'), self.sr_label_mse],
                  [QLabel('SNR'), self.sr_label_snr],
                  [QLabel('MD'), self.sr_label_md]]
        layouting(sr_layout, layout)
        # quantization
        self.quantization_steps = 8
        self.chb_quantization = QtWidgets.QCheckBox(self)
        self.cb_quantization = QtWidgets.QComboBox(self)
        self.cb_quantization.addItems(['Q2'])
        self.textb_quanztization = QtWidgets.QLineEdit(self)
        self.textb_quanztization.setText('%d' % self.quantization_steps)
        # info <= quantization
        q_layout = QVBoxLayout()
        self.q_label_mse = QLabel()
        self.q_label_snr = QLabel()
        self.q_label_md = QLabel()
        layout = [[QLabel('MSE'), self.q_label_mse],
                  [QLabel('SNR'), self.q_label_snr],
                  [QLabel('MD'), self.q_label_md]]
        layouting(q_layout, layout)

        # together
        layout = [[QLabel('Próbkowanie'), self.chb_sampling, QLabel('f'), self.textb_sampling],
                  [QLabel('Rekonstrukcja'), self.chb_reconstruction, self.cb_reconstruction],
                  sr_layout,
                  [QLabel('Kwantyzacja'), self.chb_quantization, self.cb_quantization,
                   QLabel('Poziomy kwantyzacji'), self.textb_quanztization],
                  q_layout]
        self.setLayout(layouting(main_layout, layout))
        self.connect()

    def connect(self):
        self.chb_sampling.stateChanged.connect(self.update)
        self.chb_quantization.stateChanged.connect(self.update)
        self.chb_reconstruction.stateChanged.connect(self.update)
        self.textb_sampling.returnPressed.connect(self.update)
        self.textb_quanztization.returnPressed.connect(self.update)
        self.cb_reconstruction.currentIndexChanged.connect(self.update)
        self.cb_quantization.currentIndexChanged.connect(self.update)

    def update(self):
        extras = [None, None, None]
        sims = ['c1', 'c2', 'c4']
        q_labels = [self.q_label_mse, self.q_label_snr, self.q_label_md]
        sr_labels = [self.sr_label_mse, self.sr_label_snr, self.sr_label_md]
        analog = (self.plot.alg1, self.plot.alg2, self.plot.merge_method)

        # sampling
        if self.chb_sampling.isChecked():
            x, y = s1(1 / float(self.textb_sampling.text()), *analog)
            extras[0] = [x, y, {
                'color': 'orange',
                'marker': 'o',
                'linestyle': ' ',
                'markersize': 4
            }]
            # sampling + reconstruction
            if self.chb_reconstruction.isChecked():
                x, y = reconstruction_switcher(self.cb_reconstruction.currentText()) \
                    (x, y, *analog)
                extras[2] = [x, y, {
                    'color': 'green',
                    'marker': 'o',
                    'linestyle': '-',
                    'markersize': 3
                }]
                for sim, label in zip(sims, sr_labels):
                    label.setText('{:5.5f}'.format(similarity_switcher(sim)(x, y, *analog)))
        # quantization
        if self.chb_quantization.isChecked():
            x, y = quantization_switcher(self.cb_quantization.currentText()) \
                (float(self.textb_quanztization.text()), *analog)
            extras[1] = [x, y, {
                'color': 'blue',
                'marker': 'o',
                'linestyle': '-',
                'markersize': 2
            }]
            for sim, label in zip(sims, q_labels):
                label.setText('{:5.5f}'.format(similarity_switcher(sim)(x, y, *analog)))
        self.plot.set_extras(extras)
