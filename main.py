'''
Created on 1 серп. 2013

@author: Бодя
'''

import sys

from view import *

from PySide import QtCore, QtGui

class Controller:
    def __init__(self):
        self.m = ModelMetadata()
        self.v = View()
        
        self.status = "stoped"
        
        self.v.spinColumns.valueChanged["int"].connect(lambda val: setattr(self.m, "columns", val))
        
        self.v.tabComb.currentChanged.connect(self.handleChange)
        self.v.plainNCustom.textChanged.connect(self.handleChange)
        self.v.spinN.valueChanged.connect(self.handleChange)
        self.v.spinK.valueChanged.connect(self.handleChange)
        self.v.radioN.clicked.connect(self.handleChange)
        self.v.radioNCustom.clicked.connect(self.handleChange)
        
        self.v.btnStart.clicked.connect(self.handleStart)
        self.v.btnStop.clicked.connect(self.handleStop)
    
    def run(self):
        sys.exit(app.exec_())
        
    def handleStart(self):
        if self.status in ["stoped", "paused"]:
            self.status = "started"
            
            self.v.disabledWhenStart(True)
            self.v.btnStart.setText("Призупинити")
            self.v.btnStart.setIcon(QtGui.QIcon(QtGui.QPixmap(":/icons/pause.png")))
        elif self.status == "started":
            self.status = "paused"
            
            self.v.btnStart.setText("Продовжити")
            self.v.btnStart.setIcon(QtGui.QIcon(QtGui.QPixmap(":/icons/play.png")))
            
            self.handlePause()
    
    def handlePause(self):
        pass
    
    def handleStop(self):
        self.status = "stoped"
        
        self.v.disabledWhenStart(False)
        
        self.v.btnStart.setText("Старт обчислень")
        self.v.btnStart.setIcon(QtGui.QIcon(QtGui.QPixmap(":/icons/play.png")))
        
    def handleChange(self):
        if self.v.plainNCustom.isEnabled():
            self.m.seq = self.v.plainNCustom.toPlainText().split()
            if not self.m.seq: return
            self.v.spinK.setMaximum(len(self.m.seq))
        else:
            self.m.seq = range(1, self.v.spinN.value() + 1)
            
        self.m.K = self.v.spinK.value()
        
        self.updateMetaAll()

    def updateMetaAll(self):
        self.m.All = self.v.currentTab.coreNumber(self.m.seq, self.m.K)
        self.v.MetaTableUpdate(self.m)
        #print(self.m.All)
        
        
class ModelMetadata:
    def __init__(self):
        self.seq = self.K = self.All = None
        
        self.columns = 1
        self.result = []
    
    

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    c = Controller()
    c.run()
