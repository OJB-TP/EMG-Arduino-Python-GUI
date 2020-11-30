# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 17:26:34 2020

@author: Andre
"""

from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import EMGreader

class EMGApp(QtWidgets.QMainWindow, EMGreader.Ui_MainWindow):
    def __init__(self, parent=None):
        super(EMGApp, self).__init__(parent)
        self.setupUi(self)
        
def printStartBtn():
    print("Start pressed")
    
def printStopBtn():
    print ("Stop pressed")
    
def printConnectBtn():
    print ("Connect pressed")
    
def printRecBtn():
    print ("REC pressed")
    
def main():
    app = QApplication(sys.argv)
    form = EMGApp()
    form.startButton.clicked.connect (printStartBtn)
    form.stopButton.clicked.connect (printStopBtn)
    form.connectButton.clicked.connect (printConnectBtn)
    form.recButton.clicked.connect (printRecBtn)

    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
