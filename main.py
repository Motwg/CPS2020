from PyQt5 import QtWidgets
import sys

from PyQt5.QtWidgets import QStyleFactory

from gui import Ui_MainWindow

'''
t1 = 0
d = 10
f = 0.1
A = 1
T = 2
kw = 0.5
ts = (d - t1) / 2
ns = ts / f
p = 0.03
kwargs = {
    'function': 's11',
    't1': t1,
    'd': d,
    'f': f,
    't2': d - t1,
    'A': A,
    'T': T,
    'kw': kw,
    'ts': ts,
    'ns': ns,
    'p': p
}
'''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




