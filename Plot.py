
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QSlider, QHBoxLayout, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import statistics as st


class Plot(QDialog):
    def __init__(self, parent=None):
        super(Plot, self).__init__(parent)

        self.figure = plt.figure(figsize=(15, 8))
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
        self.upper_layout = QHBoxLayout()
        self.create_labels()
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addLayout(self.upper_layout)
        layout.addWidget(self.canvas)
        layout.addWidget(self.sl_bins)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def update(self):
        self.figure.clear()

        # plot
        ax = self.figure.add_subplot(121)
        ax.plot(self.vector_x, self.vector_y, linestyle='-', marker='o', color='red', markersize=1.4)
        ax.grid(True)
        ax.margins(0.01, 0.05)

        # histogram
        ax = self.figure.add_subplot(122)
        ax.hist(self.vector_y, bins=self.sl_bins.value())
        ax.grid(True)

        self.canvas.draw()
        self.update_labels()

    def create_labels(self):
        labs = []
        for lab in ['Średnia: ', 'Bezwględna średnia: ', 'Wartość skuteczna: ', 'Wariancja: ', 'Moc średnia: ']:
            l_lab = QLabel()
            l_lab.setAlignment(Qt.AlignCenter)
            l_lab.setText(lab)
            labs.append(l_lab)

        self.l_mean = QLabel()
        self.l_mean.setAlignment(Qt.AlignCenter)
        self.upper_layout.addWidget(labs[0])
        self.upper_layout.addWidget(self.l_mean)

        self.l_absmean = QLabel()
        self.l_absmean.setAlignment(Qt.AlignCenter)
        self.upper_layout.addWidget(labs[1])
        self.upper_layout.addWidget(self.l_absmean)

        self.l_ws = QLabel()
        self.l_ws.setAlignment(Qt.AlignCenter)
        self.upper_layout.addWidget(labs[2])
        self.upper_layout.addWidget(self.l_ws)

        self.l_war = QLabel()
        self.l_war.setAlignment(Qt.AlignCenter)
        self.upper_layout.addWidget(labs[3])
        self.upper_layout.addWidget(self.l_war)

        self.l_ms = QLabel()
        self.l_ms.setAlignment(Qt.AlignCenter)
        self.upper_layout.addWidget(labs[4])
        self.upper_layout.addWidget(self.l_ms)

    def update_labels(self):
        self.l_mean.setText(str(round(st.mean(self.vector_x, self.vector_y), 2)))
        self.l_absmean.setText(str(round(st.absmean(self.vector_x, self.vector_y), 2)))
        self.l_ws.setText(str(round(st.ws(self.vector_x, self.vector_y), 2)))
        self.l_war.setText(str(round(st.war(self.vector_x, self.vector_y), 2)))
        self.l_ms.setText(str(round(st.ms(self.vector_x, self.vector_y), 2)))
