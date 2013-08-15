'''
Created on 1 серп. 2013

@author: Бодя
'''

import sys

from view import *
from mytimer import MyTimer

from PySide import QtCore, QtGui

class Controller:
    def __init__(self):
        self.m = ModelMetadata()
        self.v = View()
        self.timer = MyTimer(self.v, c = self)
        self.thread = MyThread(self.v, c = self)
        
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
        
        self.v.connect(self.thread, QtCore.SIGNAL("upd_prog_bar(int)"), self.v.progressBar, QtCore.SLOT("setValue(int)"))
        self.thread.finished.connect(lambda: print(len(self.m.result)))
        #self.v.connect(self.thread, QtCore.SIGNAL("upd_prog(int)"), self.v.MetaTableUpdateProgress)
    
    def run(self):
        sys.exit(app.exec_())
        
    def handleStart(self):
        if self.status in ["stoped", "paused"]:
            self.status = "started"
            
            self.v.disabledWhenStart(True)
            self.v.btnStart.setText("Призупинити")
            self.v.btnStart.setIcon(QtGui.QIcon(QtGui.QPixmap(":/icons/pause.png")))
            
            self.timer.start(1000)
            self.thread.start()
            
        elif self.status == "started":
            self.status = "paused"
            
            self.v.btnStart.setText("Продовжити")
            self.v.btnStart.setIcon(QtGui.QIcon(QtGui.QPixmap(":/icons/play.png")))
            
            self.handlePause()
    
    def handlePause(self):
        self.timer.stop()
    
    def handleStop(self):
        self.status = "stoped"
        
        self.v.disabledWhenStart(False)
        
        self.v.btnStart.setText("Старт обчислень")
        self.v.btnStart.setIcon(QtGui.QIcon(QtGui.QPixmap(":/icons/play.png")))
        
        if self.timer.isActive():
            self.timer.stop()
        if self.thread.isRunning():
            self.thread.quit()
        self.m.reset()
        
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
        self.seq = self.K = self.All = self.complete = 0
        
        self.time_sec = 0
        self.left_sec = 3512 # TEMP
        self.left = self.time = ""
        
        self.columns = 1
        self.result = []
        
    def reset(self):
        self.result = []
        self.complete = 0
        self.time_sec = 0
        self.left_sec = 3512 # TEMP
        self.left = self.time = ""
        
class MyThread(QtCore.QThread):
    def __init__(self, parent, c=None):
        QtCore.QThread.__init__(self, parent)
        self.c = c
        
    def run(self):
        for RES in self.c.v.currentTab.coreGenerator(self.c.m.seq, self.c.m.K):
            self.c.m.result.append(RES)
            self.c.m.complete += 1
            
            #self.emit(QtCore.SIGNAL("upd_prog_bar(int)"), round(self.c.m.complete / self.c.m.All * 100))
            #self.emit(QtCore.SIGNAL("upd_prog(int)"), self.c.m.complete)
            
            while self.c.status=="paused":
                self.msleep(500)
            
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    c = Controller()
    c.run()
