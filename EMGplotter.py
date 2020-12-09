# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 17:26:34 2020

@author: Andrea Zedda
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
from threading import Thread
from time import sleep
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import datetime; 


started = False


    
class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)
    

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            arduino = serial.Serial('COM33', 9600, timeout=.1)
        except:
            print ("can't open COM because connected")
        cnt = 0
        global started
        while started:
            ct = datetime.datetime.now()
            cnt = cnt + 1
            print (arduino.readline())
            print(cnt)
            print (ct)


class EMGApp(QtWidgets.QMainWindow, EMGreader.Ui_MainWindow):
    def __init__(self, parent=None):
        super(EMGApp, self).__init__(parent)
        self.setupUi(self)
        self.threadpool = QThreadPool()
        
    def print_output(self, s):
        print(s)
        
    def execute_this_fn():
        print("in execute")
        
        for n in range(0, 5):
            
            print ("execute")
        return "Done."
        
    def start_Thread(self):
        print ("Thread starting...")
        worker = Worker(self.execute_this_fn) 
        self.threadpool.start(worker)

def threaded_function(arg):
    for i in range(arg):
        print("running")
        sleep(1)        


def printStartBtn():
    print("Start pressed")
    Start()
    form = EMGApp()
    form.start_Thread();
    
def printStopBtn():
    print ("Stop pressed")
    Stop()
    
def printConnectBtn():
    print ("Connect pressed")
    arduino.open()
    
def printRecBtn():
    print ("REC pressed")
    
def main():
    global app
    app = QApplication(sys.argv)
    form = EMGApp()
    form.startButton.clicked.connect (printStartBtn)
    form.stopButton.clicked.connect (printStopBtn)
    form.connectButton.clicked.connect (printConnectBtn)
    form.recButton.clicked.connect (printRecBtn)
    form.show()
    app.exec_()

def Start():
    global started
    if not started:
        started = True
        print (started)
        
def Stop():
    global started
    if started:
        started = False
        print (started)   

if __name__ == '__main__':
    main()
