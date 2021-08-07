# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EMGreader.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 408)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(200, 51, 761, 261))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setBackground('w')
        #self.x = list(range(100))  # 100 time points
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(30, 50, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(30, 100, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")
        self.recButton = QtWidgets.QPushButton(self.centralwidget)
        self.recButton.setGeometry(QtCore.QRect(30, 150, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.recButton.setFont(font)
        self.recButton.setObjectName("recButton")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(30, 200, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.connectButton.setFont(font)
        self.connectButton.setObjectName("connectButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 974, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.stopButton.setText(_translate("MainWindow", "STOP"))
        self.recButton.setText(_translate("MainWindow", "REC"))
        self.connectButton.setText(_translate("MainWindow", "CONNECT"))

