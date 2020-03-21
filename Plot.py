
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from Algorithm import Algorithm


class Plot(QDialog):
    def __init__(self, parent=None):
        super(Plot, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(2, 1, 1)
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QPushButton('Refresh')
        self.button.clicked.connect(self.update)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def update(self):
        self.figure.clear()
        ax = self.figure.add_subplot(211)
        ax.plot(self.vector_x, self.vector_y, linestyle='-', marker='o', color='red', markersize=1.4)
        self.canvas.draw()
