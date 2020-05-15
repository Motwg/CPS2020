
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QSlider, QHBoxLayout, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from core import statistics as st


class Plot(QDialog):
    def __init__(self, parent=None):
        super(Plot, self).__init__(parent)

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

        # set the layout
        self.upper_layout = QVBoxLayout()
        self.create_labels()
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addLayout(self.upper_layout)
        layout.addWidget(self.canvas)

        layout.addWidget(self.sl_bins)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.vector_x, self.vector_y, self.alg1, self.alg2, self.merge_method= None, None, None, None, None
        self.extras = [None, None, None]

    def update(self):
        if self.alg2 is None:
            self.vector_x, self.vector_y = self.alg1.perform_algorithm()
        else:
            self.vector_x, self.vector_y = self.merge_method(self.alg1, self.alg2)
        self.figure.clear()

        # plot
        ax = self.figure.add_subplot(121)
        ax.plot(self.vector_x, self.vector_y, linestyle='-', marker='o', color='red', markersize=1.4)
        for extra in self.extras:
            if extra is not None:
                ax.plot(extra[0], extra[1], **extra[2])
        ax.grid(True)
        ax.margins(0.01, 0.05)
        ax.set_xlabel('t[s]')

        # histogram
        ax = self.figure.add_subplot(122)
        ax.hist(self.vector_y, bins=self.sl_bins.value())
        ax.grid(True)

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
        mean_layout.addSpacing(600)
        self.upper_layout.addLayout(mean_layout)

        self.l_absmean = QLabel()
        self.l_absmean.setAlignment(Qt.AlignLeft)
        abs_layout = QHBoxLayout()
        abs_layout.addWidget(labs[1])
        abs_layout.addWidget(self.l_absmean)
        abs_layout.addSpacing(600)
        self.upper_layout.addLayout(abs_layout)

        self.l_ws = QLabel()
        self.l_ws.setAlignment(Qt.AlignLeft)
        ws_layout = QHBoxLayout()
        ws_layout.addWidget(labs[2])
        ws_layout.addWidget(self.l_ws)
        ws_layout.addSpacing(600)
        self.upper_layout.addLayout(ws_layout)

        self.l_war = QLabel()
        self.l_war.setAlignment(Qt.AlignLeft)
        war_layout = QHBoxLayout()
        war_layout.addWidget(labs[3])
        war_layout.addWidget(self.l_war)
        war_layout.addSpacing(600)
        self.upper_layout.addLayout(war_layout)

        self.l_ms = QLabel()
        self.l_ms.setAlignment(Qt.AlignLeft)
        ms_layout = QHBoxLayout()
        ms_layout.addWidget(labs[4])
        ms_layout.addWidget(self.l_ms)
        ms_layout.addSpacing(600)
        self.upper_layout.addLayout(ms_layout)

    def update_labels(self):
        self.l_mean.setText(str(round(st.mean(self.vector_y), 2)))
        self.l_absmean.setText(str(round(st.absmean(self.vector_y), 2)))
        self.l_ws.setText(str(round(st.ws(self.vector_y), 2)))
        self.l_war.setText(str(round(st.war(self.vector_y), 2)))
        self.l_ms.setText(str(round(st.ms(self.vector_y), 2)))
