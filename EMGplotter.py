# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 17:26:34 2020

@author: Andre
"""

from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import EMGreader

class EMGApp(QtWidgets.QMainWindow, EMGreader.Ui_MainWindow):
    def __init__(self, parent=None):
        super(EMGApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = EMGApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()