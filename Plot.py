
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QSlider
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


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
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
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
