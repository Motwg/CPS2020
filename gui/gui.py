# -*- coding: utf-8 -*-

import os

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileSystemModel, QLineEdit

from core.algorithm import Algorithm
from core.merging import merge_switcher
from gui.conversion_tab import ConversionTab
from gui.convolution_tab import ConvolutionTab
from gui.transformation_tab import TransformationTab
from plots.plot import Plot


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(608, 408)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 571, 351))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab = QtWidgets.QWidget()
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 0, 241, 331))
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 20, 160, 301))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout.addWidget(self.label)
        self.horizontalSlider_t1 = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_t1.setMaximum(9)
        self.horizontalSlider_t1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalLayout.addWidget(self.horizontalSlider_t1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout_3.addWidget(self.label_5)
        self.horizontalSlider_d = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_d.setMinimum(1)
        self.horizontalSlider_d.setMaximum(10)
        self.horizontalSlider_d.setSingleStep(1)
        self.horizontalSlider_d.setSliderPosition(1)
        self.horizontalSlider_d.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalLayout_3.addWidget(self.horizontalSlider_d)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout_3.addWidget(self.label_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout_4.addWidget(self.label_7)
        self.horizontalSlider_f = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_f.setMinimum(1)
        self.horizontalSlider_f.setMaximum(1000)
        self.horizontalSlider_f.setSliderPosition(100)
        self.horizontalSlider_f.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalLayout_4.addWidget(self.horizontalSlider_f)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout_4.addWidget(self.label_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout_5.addWidget(self.label_9)
        self.horizontalSlider_A = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_A.setSliderPosition(1)
        self.horizontalSlider_A.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalLayout_5.addWidget(self.horizontalSlider_A)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout_5.addWidget(self.label_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout_6.addWidget(self.label_11)
        self.horizontalSlider_T = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_T.setMinimum(1)
        self.horizontalSlider_T.setMaximum(1000)
        self.horizontalSlider_T.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalLayout_6.addWidget(self.horizontalSlider_T)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout_6.addWidget(self.label_12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout_7.addWidget(self.label_13)
        self.horizontalSlider_kw = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_kw.setMaximum(100)
        self.horizontalSlider_kw.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalLayout_7.addWidget(self.horizontalSlider_kw)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout_7.addWidget(self.label_14)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout_8.addWidget(self.label_15)
        self.horizontalSlider_ts = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_ts.setMaximum(199)
        self.horizontalSlider_ts.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalLayout_8.addWidget(self.horizontalSlider_ts)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout_8.addWidget(self.label_16)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout_10.addWidget(self.label_19)
        self.horizontalSlider_ns = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_ns.setMaximum(9999)
        self.horizontalSlider_ns.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalLayout_10.addWidget(self.horizontalSlider_ns)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout_10.addWidget(self.label_20)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout_9.addWidget(self.label_17)
        self.horizontalSlider_p = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_p.setMaximum(100)
        self.horizontalSlider_p.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalLayout_9.addWidget(self.horizontalSlider_p)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.horizontalLayout_9.addWidget(self.label_18)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 16, 301))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.label_23)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.label_22)
        self.label_29 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.label_30)
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.label_25)
        self.label_28 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.label_28)
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.label_26)
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.label_24)
        self.label_27 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.label_27)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(25, 20, 41, 301))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_t1 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_t1.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_4.addWidget(self.label_t1)
        self.label_d = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_d.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_4.addWidget(self.label_d)
        self.label_f = QLineEdit(self.verticalLayoutWidget_4)
        self.label_f.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_4.addWidget(self.label_f)
        self.label_A = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_A.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_4.addWidget(self.label_A)
        self.label_T = QLineEdit(self.verticalLayoutWidget_4)
        self.label_T.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_4.addWidget(self.label_T)
        self.label_kw = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_kw.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_4.addWidget(self.label_kw)
        self.label_ts = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_ts.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_4.addWidget(self.label_ts)
        self.label_ns = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_ns.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_4.addWidget(self.label_ns)
        self.label_p = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_p.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_4.addWidget(self.label_p)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 291, 271))
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 277, 249))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setAcceptDrops(False)
        self.radioButton_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_4.setAutoFillBackground(False)
        self.verticalLayout.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.radioButton_9)
        self.radioButton_10 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.radioButton_11)
        self.btn_save = QtWidgets.QPushButton(self.tab)
        self.btn_save.setGeometry(QtCore.QRect(20, 290, 75, 23))
        self.btn_load = QtWidgets.QPushButton(self.tab)
        self.btn_load.setGeometry(QtCore.QRect(210, 290, 75, 23))
        self.tabWidget.addTab(self.tab, "")

        self.plot = Plot()
        self.plot.show()

        # tab 'Scal sygnały'
        self.tab_2 = QtWidgets.QWidget()
        self.list_left = QtWidgets.QListView(self.tab_2)
        self.list_left.setGeometry(QtCore.QRect(20, 20, 191, 191))
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(240, 190, 81, 23))
        self.list_right = QtWidgets.QListView(self.tab_2)
        self.list_right.setGeometry(QtCore.QRect(350, 20, 191, 191))
        self.cb_method = QtWidgets.QComboBox(self.tab_2)
        self.cb_method.setGeometry(QtCore.QRect(250, 120, 61, 22))
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 240, 81, 23))
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 270, 81, 23))
        # Label Uwaga!
        self.label_tab2 = QtWidgets.QLabel(self.tab_2)
        self.label_tab2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tab2.move(140, 300)
        self.tabWidget.addTab(self.tab_2, "")

        # tab 'Konwersja'
        self.tab_3 = ConversionTab(self.plot)
        self.tabWidget.addTab(self.tab_3, "")

        # tab 'Sploty'
        self.tab_4 = ConvolutionTab(self.plot)
        self.tabWidget.addTab(self.tab_4, "")

        # tab 'Transformacje'
        self.tab_5 = TransformationTab(self.plot)
        self.tabWidget.addTab(self.tab_5, "")

        # finalise
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.connect()

    def connect(self):
        self.tabWidget.setCurrentIndex(0)
        self.fc_kwargs = {
            'function': 's3'
        }
        self.update()
        self.radioButton_1.fc = 's1'
        self.radioButton_2.fc = 's2'
        self.radioButton_3.fc = 's3'
        self.radioButton_4.fc = 's4'
        self.radioButton_5.fc = 's5'
        self.radioButton_6.fc = 's6'
        self.radioButton_7.fc = 's7'
        self.radioButton_8.fc = 's8'
        self.radioButton_9.fc = 's9'
        self.radioButton_10.fc = 's10'
        self.radioButton_11.fc = 's11'
        self.radioButton_3.setChecked(True)
        self.radioButton_1.toggled.connect(self.on_radio)
        self.radioButton_2.toggled.connect(self.on_radio)
        self.radioButton_3.toggled.connect(self.on_radio)
        self.radioButton_4.toggled.connect(self.on_radio)
        self.radioButton_5.toggled.connect(self.on_radio)
        self.radioButton_6.toggled.connect(self.on_radio)
        self.radioButton_7.toggled.connect(self.on_radio)
        self.radioButton_8.toggled.connect(self.on_radio)
        self.radioButton_9.toggled.connect(self.on_radio)
        self.radioButton_10.toggled.connect(self.on_radio)
        self.radioButton_11.toggled.connect(self.on_radio)
        self.horizontalSlider_t1.valueChanged.connect(self.update)
        self.horizontalSlider_d.valueChanged.connect(self.update)
        self.horizontalSlider_f.valueChanged.connect(self.update)
        self.horizontalSlider_A.valueChanged.connect(self.update)
        self.horizontalSlider_T.valueChanged.connect(self.update)
        self.horizontalSlider_kw.valueChanged.connect(self.update)
        self.horizontalSlider_ts.valueChanged.connect(self.update)
        self.horizontalSlider_ns.valueChanged.connect(self.update)
        self.horizontalSlider_p.valueChanged.connect(self.update)
        self.btn_save.clicked.connect(self.file_save)
        self.btn_load.clicked.connect(self.file_load)
        self.cb_method.addItems(['+', '-', '*', '/', '(h * x)(n)'])
        self.pushButton.clicked.connect(self.on_merge)
        self.label_f.returnPressed.connect(self.on_f_field_change)
        self.label_T.returnPressed.connect(self.on_f_field_change)

        path = QDir.current().path() + '/files/'
        self.fileModel = QFileSystemModel()
        self.fileModel.setRootPath(QDir.rootPath())
        self.list_left.setModel(self.fileModel)
        self.list_left.setRootIndex(self.fileModel.index(path))
        self.list_right.setModel(self.fileModel)
        self.list_right.setRootIndex(self.fileModel.index(path))

    # on radio button click
    def on_radio(self):
        radio_button = self.centralwidget.sender()
        if radio_button.isChecked():
            self.fc_kwargs['function'] = radio_button.fc
            self.prepare_plot()

    # on change in f field
    def on_f_field_change(self):
        value = float(self.label_f.text())
        self.horizontalSlider_f.setValue(int(value))
        value = float(self.label_T.text())
        self.horizontalSlider_T.setValue(int(value))
        self.update()

    def update(self):
        self.fc_kwargs['t1'] = self.horizontalSlider_t1.value()
        self.fc_kwargs['d'] = self.horizontalSlider_d.value()
        self.fc_kwargs['f'] = 1 / self.horizontalSlider_f.value()
        self.fc_kwargs['t2'] = self.horizontalSlider_d.value() - self.horizontalSlider_t1.value()
        self.fc_kwargs['A'] = self.horizontalSlider_A.value()
        self.fc_kwargs['T'] = self.horizontalSlider_T.value()
        self.fc_kwargs['T'] = 1 / self.horizontalSlider_T.value()
        self.fc_kwargs['kw'] = self.horizontalSlider_kw.value() / 100
        self.fc_kwargs['ts'] = self.horizontalSlider_ts.value()
        self.fc_kwargs['ns'] = self.horizontalSlider_ns.value()
        self.fc_kwargs['p'] = self.horizontalSlider_p.value() / 100
        self.label_t1.setText(str(self.fc_kwargs['t1']))
        self.label_d.setText(str(self.fc_kwargs['d']))
        self.label_f.setText('{:.1f}'.format(self.horizontalSlider_f.value()))
        self.label_A.setText(str(self.fc_kwargs['A']))
        self.label_T.setText('{:.1f}'.format(self.horizontalSlider_T.value()))
        self.label_kw.setText(str(self.fc_kwargs['kw']))
        self.label_ts.setText(str(self.fc_kwargs['ts']))
        self.label_ns.setText(str(self.fc_kwargs['ns']))
        self.label_p.setText(str(self.fc_kwargs['p']))
        self.prepare_plot()

    # should be used after every single signal adjustments
    def prepare_plot(self):
        self.alg = Algorithm(**self.fc_kwargs)
        self.plot.set_alg(self.alg)
        self.tab_3.update()
        self.tab_4.update()
        self.tab_5.update()

    # single signal save
    def file_save(self):
        os.makedirs(os.getcwd() + '/files', exist_ok=True)
        name = QtWidgets.QFileDialog.getSaveFileName(
            self.centralwidget, 'Save File', './files', '*.json')
        if name[0] != '':
            self.alg.save_algorithm(name[0].split('/')[-1])

    # single signal load
    def file_load(self):
        os.makedirs(os.getcwd() + '/files', exist_ok=True)
        name = QtWidgets.QFileDialog.getOpenFileName(
            self.centralwidget, 'Open File', './files', '*.json')
        if name[0] != '':
            self.alg = Algorithm(**self.fc_kwargs)
            self.alg.load_algorithm(name[0].split('/')[-1])
            self.plot.set_alg(self.alg)

    # on 'Scal' button
    def on_merge(self):
        # if nothing is selected skip
        if len(self.list_left.selectedIndexes()) == 0 or len(self.list_right.selectedIndexes()) == 0:
            return
        right = self.list_right.selectedIndexes()[0]
        left = self.list_left.selectedIndexes()[0]
        alg1 = Algorithm(**self.fc_kwargs)
        alg2 = Algorithm(**self.fc_kwargs)
        alg1.load_algorithm(left.data())
        alg2.load_algorithm(right.data())
        self.plot.merge_method = merge_switcher(self.cb_method.currentText())
        self.plot.set_alg(alg1, alg2)
        self.tab_3.update()
        self.tab_4.update()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CPS"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Parametry sygnału"))
        self.label.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "9 [s]"))
        self.label_5.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow", "10 [s]"))
        self.label_7.setText(_translate("MainWindow", "1"))
        self.label_8.setText(_translate("MainWindow", "1000 [Hz]"))
        self.label_9.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "100"))
        self.label_11.setText(_translate("MainWindow", "1"))
        self.label_12.setText(_translate("MainWindow", "1000 [Hz]"))
        self.label_13.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "1"))
        self.label_15.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "199"))
        self.label_19.setText(_translate("MainWindow", "0"))
        self.label_20.setText(_translate("MainWindow", "9999"))
        self.label_17.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "1"))
        self.label_23.setText(_translate("MainWindow", "t1"))
        self.label_22.setText(_translate("MainWindow", "d"))
        self.label_29.setText(_translate("MainWindow", "f"))
        self.label_30.setText(_translate("MainWindow", "A"))
        self.label_25.setText(_translate("MainWindow", "T"))
        self.label_28.setText(_translate("MainWindow", "kw"))
        self.label_26.setText(_translate("MainWindow", "ts"))
        self.label_24.setText(_translate("MainWindow", "ns"))
        self.label_27.setText(_translate("MainWindow", "p"))
        self.label_t1.setText(_translate("MainWindow", "t1"))
        self.label_d.setText(_translate("MainWindow", "d"))
        self.label_f.setText(_translate("MainWindow", "f"))
        self.label_A.setText(_translate("MainWindow", "A"))
        self.label_T.setText(_translate("MainWindow", "T"))
        self.label_kw.setText(_translate("MainWindow", "kw"))
        self.label_ts.setText(_translate("MainWindow", "ts"))
        self.label_ns.setText(_translate("MainWindow", "ns"))
        self.label_p.setText(_translate("MainWindow", "p"))
        self.label_tab2.setText(_translate("MainWindow", "UWAGA! Parametry t1, d i f są przejmowane z lewego sygnału!"))
        self.groupBox.setTitle(_translate("MainWindow", "Sygnały"))
        self.radioButton_1.setText(_translate("MainWindow", "Szum o rozkładzie jednostajnym"))
        self.radioButton_2.setText(_translate("MainWindow", "Szum gaussowski"))
        self.radioButton_3.setText(_translate("MainWindow", "Sygnał sinusoidalny"))
        self.radioButton_4.setText(_translate("MainWindow", "Sygnał sinusoidalny wyprostowany jednopołówkowo"))
        self.radioButton_5.setText(_translate("MainWindow", "Sygnał sinusoidalny wyprostowany dwupołówkowo"))
        self.radioButton_6.setText(_translate("MainWindow", "Sygnał prostokątny"))
        self.radioButton_7.setText(_translate("MainWindow", "Sygnał prostokątny symetryczny"))
        self.radioButton_8.setText(_translate("MainWindow", "Sygnał trójkątny"))
        self.radioButton_9.setText(_translate("MainWindow", "Skok jednostkowy"))
        self.radioButton_10.setText(_translate("MainWindow", "Impuls jednostkowy"))
        self.radioButton_11.setText(_translate("MainWindow", "Szum impulsowy"))
        self.btn_save.setText(_translate("MainWindow", "Zapisz"))
        self.btn_load.setText(_translate("MainWindow", "Wczytaj"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Nowy sygnał"))
        self.pushButton.setText(_translate("MainWindow", "Scal"))
        self.pushButton_2.setText(_translate("MainWindow", "Zapisz"))
        self.pushButton_3.setText(_translate("MainWindow", "Wczytaj"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Scal sygnały"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Konwersja"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Sploty"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Transformacje"))