from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QComboBox, QLabel

from core.merging import perform_merge
from core.utils import split_complex
from gui.utils import layouting
from transformation.sample_signals import signal_switcher
from transformation.transformation import transformation_switcher


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
        self.cb_transformation.addItems(['DFT', 'F2', 'T3'])

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
        extras = [None, None]
        extras_i = [None, None]
        if self.chb_signal.isChecked():
            self.plot.alg1.kwargs['f'] = 1 / 16
            self.plot.alg1.kwargs['function'] = signal_switcher(self.cb_signal.currentText())

        if self.chb_transformation.isChecked():
            method, i_method = transformation_switcher(self.cb_transformation.currentText())
            v_x, v_y = perform_merge(self.plot.alg1, self.plot.alg2, self.plot.merge_method)
            transformed_y = method(v_y)
            real_transformed_y, imag_transformed_y = split_complex(transformed_y, self.plot.cb_plot.currentText())
            extras[0] = (v_x, real_transformed_y, {
                     'color': 'blue',
                     'marker': 'o',
                     'linestyle': (0, (5, 10)),
                     'markersize': 3
                 })
            extras_i[0] = (v_x, imag_transformed_y, {
                     'color': 'blue',
                     'marker': 'o',
                     'linestyle': (0, (5, 10)),
                     'markersize': 3
                 })
            if self.chb_i_transformation.isChecked():
                transformed_y = i_method(transformed_y)
                real_transformed_y, imag_transformed_y = split_complex(transformed_y, self.plot.cb_plot.currentText())
                extras[1] = (v_x, real_transformed_y, {
                    'color': 'orange',
                    'marker': 'o',
                    'linestyle': (0, (5, 10)),
                    'markersize': 3
                })
                extras_i[1] = (v_x, imag_transformed_y, {
                    'color': 'orange',
                    'marker': 'o',
                    'linestyle': (0, (5, 10)),
                    'markersize': 3
                })
        self.plot.set_extras(extras, extras_i)
