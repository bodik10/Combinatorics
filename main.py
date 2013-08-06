'''
Created on 1 серп. 2013

@author: Бодя
'''
import sys

from core import *
from view import *

from PySide import QtCore, QtGui

class Controller:
    def __init__(self):
        self.v = View()
        
    def run(self):
        sys.exit(app.exec_())



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    c = Controller()
    c.run()