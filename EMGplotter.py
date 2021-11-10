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
import numpy as np;
import pathlib;
from datetime import datetime as dt

started = False
ct = 0
generalDebug = True
listDebug = False 
receivingDebug = True  
global recBool
recBool = False 
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
        arduino = serial.Serial('COM3', 115200)
        try:
            arduino = serial.Serial('COM3', 115200)
        except:
            print ("can't open COM because connected")
        cnt = 0
        total_time_elapsed = 0
        ct = time.time()
        samples = 100
        packet_size = 3
        incoming_buffer = samples * packet_size
        global started
        global form
        global app
        L = [1,2,3,4,5,1,2,3,4]
        thisPlot = form.graphicsView.plot(L)
        L2 = [4,3,2,1,5,4,3,2,1]
        avgPlot = form.graphicsView.plot(L2)
        FreqSamp = 1000 
        seconds = 5
        points = FreqSamp * seconds
        thisPlot.x = list(range(1, points+1))
        thisPlot.y = [0] * points
        begin = 1
        # opening file
        file_date = dt.today().strftime("%b-%d-%Y")
        print (str(file_date))
        file_path=os.path.join(str(pathlib.Path().parent.resolve()), "EMG" + str(file_date) + str(time.time()) + ".txt")
        #print (file_path)
        #file_name = os.path.join(this_path, file_date + ".txt")
        print ("Writing in this path: " + file_path)
        f = open(file_path, "a")
        global recBool
        while started:
            #time.sleep(samples/1000)
            delta = time.time() - ct
            ct = time.time()
            #ct = datetime.datetime.now()
            cnt = cnt + 1
            inc_bytes = bytes(arduino.read(incoming_buffer))            
            #print (inc_bytes)
            tmp_int = ConvertBufferToData(inc_bytes, samples)
            #x = list(range(1, len (tmp_int)))
            if tmp_int != None:
                redTmp_int = [i for i in tmp_int if i]
                ##WIP
                print (redTmp_int)
                if recBool:
                    total_time_elapsed += delta
                    for row in redTmp_int:
                        if delta != 0:#np.savetxt(f, row)
                            toWrite = str(row) + "," + str(total_time_elapsed) + ","  + str((1/delta))  + "," + str(len(redTmp_int)) + ","+ str(len(redTmp_int)/(delta)) + "," + "\n"
                            f.write(toWrite)
                else:
                    f.close()
                stopEnd = begin + len(redTmp_int)
                if stopEnd > points:
                        begin = 0
                        stopEnd = begin + len(redTmp_int)
                #print ("stopEnd: "+ str(stopEnd))
                #print ("thisPlot.y: "+ str(thisPlot.y))
                #print ("redTmp_int: "+ str(redTmp_int))

                thisPlot.y [begin:stopEnd] = redTmp_int
                thisPlot.setData(thisPlot.x, thisPlot.y, pen=pg.mkPen('b', width=5))
                #form.graphicsView.enableAutoScale()

                #this.Plot.setXRange(5, 4990)
                #WIP
                begin = begin + len(redTmp_int)
            if delta != 0:
                
                if generalDebug and receivingDebug:
                    print ("Elapsed time in receiving: " + str(delta * 1000) + "ms")
                    print ("Frequenza di ricezione del package: " + str((1/delta)) + "Hz")
                    print ("Number of samples received: " + str(len(redTmp_int)))
                    print ("Estimated sample frequency: " + str(len(redTmp_int)/(delta)))
            print(cnt)
            print (datetime.datetime.now())


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
    global recBool
    if recBool:
        recBool = False
    else:
        recBool = True
    
def main():
    global app
    app = QApplication(sys.argv)
    global form
    form = EMGApp()
    form.startButton.clicked.connect (printStartBtn)
    form.stopButton.clicked.connect (printStopBtn)
    form.connectButton.clicked.connect (printConnectBtn)
    form.recButton.clicked.connect (printRecBtn)
    
    L = []
    form.graphicsView.plot(L, pen=pg.mkPen('b', width=5))
    form.graphicsView.enableAutoScale()
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

def ConvertBufferToData (tmp_bytes, samples):
    if generalDebug and listDebug: print (len(tmp_bytes))
    ff_indexes = [i for i, x in enumerate(tmp_bytes) if x == 0xFF]
    diff_ff_indexes = np.diff(ff_indexes)
    wrong_diff = [i for i, x in enumerate(diff_ff_indexes) if x != 3]
    if generalDebug and listDebug: print ("ff_ indexes: " + str(ff_indexes))
    if generalDebug and listDebug: print ("diff_ff_indexes: " + str (diff_ff_indexes))
    if (ff_indexes[0]+3==ff_indexes[1] and ff_indexes[1]+3==ff_indexes[2]):
        int_index = 0
        tmp_int = [None]*samples
        diff_index = 0
        for ff_index in ff_indexes:
            if generalDebug and listDebug: print ("diff_index: " +str(diff_index))
            if diff_index<len(diff_ff_indexes):
                if diff_ff_indexes[diff_index] < 3: 
                    diff_index = diff_index + 1
                    continue
                diff_index = diff_index + 1
            if generalDebug and listDebug: print ("ff_index: " + str(ff_index))
            if generalDebug and listDebug: print ("converting: " + str(tmp_bytes[(ff_index+1) : (ff_index+3)]))
            tmp_int[int_index] = int.from_bytes(tmp_bytes[(ff_index+1):(ff_index+3)], byteorder ='big')
            if generalDebug and listDebug: print("tmp_int[int_index]: " + str(tmp_int[int_index]))
            int_index = int_index + 1
        if generalDebug: print (str(tmp_int))
        return tmp_int
    else:
        if generalDebug: print ("Bad packet")
        return
    
def update_plot_data(plotParam, indexParam, yParam):
    FreqSamp = 1000 
    packet_size = 3
    seconds = 5
    points = FreqSamp * packet_size * seconds
    plotParam.x = list(range(1, points))
    yParam 
    plotParam.y.append(yParam)  # Add a new value.
    
    plotParam.data_line.setData(plotParam.x, plotParam.y)  # Update the data.    

    
    
if __name__ == '__main__':
    main()
