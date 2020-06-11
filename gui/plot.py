import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QSlider, QHBoxLayout, QLabel, QComboBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from core import statistics as st
from core.merging import perform_merge
from core.utils import split_complex


class Plot(QDialog):
    def __init__(self, parent=None):
        super(Plot, self).__init__(parent)
        self.resize(1200, 600)

        self.figure = plt.figure(figsize=(10, 4))
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.button = QPushButton('Refresh')
        self.button.clicked.connect(self.update)

        self.sl_bins = QSlider()
        self.sl_bins.setMinimum(5)
        self.sl_bins.setMaximum(20)
        self.sl_bins.setSingleStep(1)
        self.sl_bins.setSliderPosition(10)
        self.sl_bins.setOrientation(Qt.Horizontal)
        self.sl_bins.setTickInterval(0)
        self.sl_bins.valueChanged.connect(self.update)

        self.cb_plot = QComboBox(self)
        self.cb_plot.addItems(['W1', 'W2'])
        self.cb_plot.currentIndexChanged.connect(self.update)

        self.cb_hist = QComboBox(self)
        self.cb_hist.addItems(['Img plot', 'Histogram'])
        self.cb_hist.currentIndexChanged.connect(self.update)

        # set the upper layout
        upper_layout = QHBoxLayout()
        upper_layout.addLayout(self.create_labels())
        upper_right_layout = QVBoxLayout()
        upper_right_layout.addWidget(self.cb_plot)
        upper_right_layout.addWidget(self.cb_hist)
        upper_layout.addLayout(upper_right_layout)

        # set overall layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addLayout(upper_layout)
        layout.addWidget(self.canvas)
        layout.addWidget(self.sl_bins)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.show_main = True
        self.vector_x, self.vector_y, self.vector_i = None, None, None
        self.alg1, self.alg2, self.merge_method = None, None, None
        self.extras = [None, None, None]

    def update(self):
        self.figure.clear()
        self.vector_x, self.vector_y = perform_merge(self.alg1, self.alg2, self.merge_method)
        self.vector_y, self.vector_i = split_complex(self.vector_y, self.cb_plot.currentText())

        # plot
        ax = self.figure.add_subplot(211)
        ax_i = self.figure.add_subplot(212)
        if self.show_main:
            ax.plot(self.vector_x, self.vector_y, linestyle='-', marker='o', color='red', markersize=1.4)
            ax.grid(True)
            ax.margins(0.01, 0.05)
            ax.set_xlabel('t[s]')

            if self.cb_hist.currentText() == 'Img plot':
                # imaginary plot
                ax_i.plot(self.vector_x, self.vector_i, linestyle='-', marker='o', color='red', markersize=1.4)
                ax_i.grid(True)
                ax_i.margins(0.01, 0.05)
                ax_i.set_xlabel('t[s]')
            else:
                # histogram
                ax_i = self.figure.add_subplot(313)
                ax_i.hist(self.vector_y, bins=self.sl_bins.value())
                ax_i.grid(True)

        for extra in self.extras:
            if extra is not None:
                ax.plot(extra[0], extra[1], **extra[2])

        self.canvas.draw()
        self.update_labels()

    def set_alg(self, alg1, alg2=None):
        self.alg1 = alg1
        self.alg2 = alg2
        self.update()

    def set_extras(self, extras):
        self.extras = extras
        self.update()

    def create_labels(self):
        labs = []
        upper_left_layout = QVBoxLayout()
        for lab in ['Średnia: ', 'Bezwględna średnia: ', 'Wartość skuteczna: ', 'Wariancja: ', 'Moc średnia: ']:
            l_lab = QLabel()
            l_lab.setAlignment(Qt.AlignLeft)
            l_lab.setText(lab)
            labs.append(l_lab)

        self.l_mean = QLabel()
        self.l_mean.setAlignment(Qt.AlignLeft)
        mean_layout = QHBoxLayout()
        mean_layout.addWidget(labs[0])
        mean_layout.addWidget(self.l_mean)
        mean_layout.addSpacing(900)
        upper_left_layout.addLayout(mean_layout)

        self.l_absmean = QLabel()
        self.l_absmean.setAlignment(Qt.AlignLeft)
        abs_layout = QHBoxLayout()
        abs_layout.addWidget(labs[1])
        abs_layout.addWidget(self.l_absmean)
        abs_layout.addSpacing(900)
        upper_left_layout.addLayout(abs_layout)

        self.l_ws = QLabel()
        self.l_ws.setAlignment(Qt.AlignLeft)
        ws_layout = QHBoxLayout()
        ws_layout.addWidget(labs[2])
        ws_layout.addWidget(self.l_ws)
        ws_layout.addSpacing(900)
        upper_left_layout.addLayout(ws_layout)

        self.l_war = QLabel()
        self.l_war.setAlignment(Qt.AlignLeft)
        war_layout = QHBoxLayout()
        war_layout.addWidget(labs[3])
        war_layout.addWidget(self.l_war)
        war_layout.addSpacing(900)
        upper_left_layout.addLayout(war_layout)

        self.l_ms = QLabel()
        self.l_ms.setAlignment(Qt.AlignLeft)
        ms_layout = QHBoxLayout()
        ms_layout.addWidget(labs[4])
        ms_layout.addWidget(self.l_ms)
        ms_layout.addSpacing(900)
        upper_left_layout.addLayout(ms_layout)

        return upper_left_layout

    def update_labels(self):
        self.l_mean.setText(str(round(st.mean(self.vector_y), 2)))
        self.l_absmean.setText(str(round(st.absmean(self.vector_y), 2)))
        self.l_ws.setText(str(round(st.ws(self.vector_y), 2)))
        self.l_war.setText(str(round(st.war(self.vector_y), 2)))
        self.l_ms.setText(str(round(st.ms(self.vector_y), 2)))
