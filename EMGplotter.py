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
import sys
import os
import EMGreader
import serial
import time
from guiLoop import guiLoop, stopLoop

started = False
arduino = serial.Serial('COM33', 9600, timeout=.1)

class EMGApp(QtWidgets.QMainWindow, EMGreader.Ui_MainWindow):
    def __init__(self, parent=None):
        super(EMGApp, self).__init__(parent)
        self.setupUi(self)
        


def printStartBtn():
    print("Start pressed")
    started = True
    StartLoop(EMGreader.Ui_MainWindow)
    
def printStopBtn():
    print ("Stop pressed")
    Stop
    
def printConnectBtn():
    print ("Connect pressed")
    arduino.open()
    
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

def Start():
    if not started:
        # you can also use threads here, see the first link
        started = True
        print (started)
        
def Stop():
    if started:
        #stopLoop(self.started)
        started = False
        print (started)

@guiLoop
def StartLoop():
        # This is your Start function
        # ...
        print ("in startloop")
        while True:
            print (arduino.readline())    

if __name__ == '__main__':
    main()
