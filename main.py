'''
Created on 1 серп. 2013

@author: Бодя
'''

import sys

from view import *
from mytimer import MyTimer
from mythread import MyThread

from PySide import QtCore, QtGui

class Controller(QtGui.QWidget, View):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setupUi(self)
        
        self.title = "Combinatorics - Обчислення комбінацій та перестановок" 
        self.currentTabText = self.tabComb.tabText(self.tabComb.currentIndex())
        self.currentTab = self.tabComb.currentWidget()
        self.setWindowTitle(self.title + " - " + self.currentTabText)
        
        self.m = ModelMetadata()
        #self.v = self
        self.timer = MyTimer(self)
        self.thread = MyThread(self)
        
        self.status = "stoped"
        
        self.handleEvents()
        self.MetaTableReset()

        self.show()
    
    def run(self):
        sys.exit(app.exec_())

    def handleEvents(self):
        # enable/disable spinBox or plainTextEdit
        self.connect(self.radioN, QtCore.SIGNAL("toggled(bool)"), self.spinN.setEnabled)
        self.connect(self.radioNCustom, QtCore.SIGNAL("toggled(bool)"), self.plainNCustom.setEnabled)

        self.tabComb.currentChanged.connect(self.handleChangeTab)
        
        # link in QLabel leads to other Tab within QTabWidget
        self.label.linkActivated.connect(lambda link: self.tabComb.setCurrentIndex(int(link[4:])))

        # prevent setting K larger than N
        self.spinN.valueChanged.connect(lambda value: self.spinK.setMaximum(value))


        self.spinColumns.valueChanged["int"].connect(lambda val: setattr(self.m, "columns", val))
        
        self.tabComb.currentChanged.connect(self.handleChange)
        self.plainNCustom.textChanged.connect(self.handleChange)
        self.spinN.valueChanged.connect(self.handleChange)
        self.spinK.valueChanged.connect(self.handleChange)
        self.radioN.clicked.connect(self.handleChange)
        self.radioNCustom.clicked.connect(self.handleChange)
        
        self.btnStart.clicked.connect(self.handleStart)
        self.btnStop.clicked.connect(self.handleStop)
        
        self.connect(self.thread, QtCore.SIGNAL("upd_prog_bar(int)"), self.metaRows["progressBar"], QtCore.SLOT("setValue(int)"))
        self.thread.finished.connect(lambda: print(len(self.m.result)))
        #self.connect(self.thread, QtCore.SIGNAL("upd_prog(int)"), self.MetaProgressUpdate)

    def handleChange(self):
        if self.plainNCustom.isEnabled():
            self.m.seq = self.plainNCustom.toPlainText().split()
            if not self.m.seq: return
            self.spinK.setMaximum(len(self.m.seq))
        else:
            self.m.seq = range(1, self.spinN.value() + 1)
            
        self.m.K = self.spinK.value()
        
        self.MetaAllUpdate()
        
    def handleChangeTab(self, index):
        self.currentTabText = self.tabComb.tabText(index)
        self.currentTab = self.tabComb.widget(index)
        self.setWindowTitle(self.title + " - " + self.currentTabText)
        
        self.spinK.setDisabled(index==4) # Permutation doesn't require K, only N
        
        self.MetaTableReset()
        
    def disabledWhenStart(self, flag):
        # list of elements that gonna be disabled when Calc. starts (and enabled when stops)
        disableList = [self.tabComb, self.groupInput, self.checkMetadata, self.checkShowResult, self.spinColumns, self.btnResultPath]
        
        self.btnStop.setEnabled(flag)
        
        for w in disableList:
            w.setDisabled(flag)
        
    def handleStart(self):
        if self.status in ["stoped", "paused"]:
            self.status = "started"
            
            self.disabledWhenStart(True)
            self.btnStart.setText("Призупинити")
            self.btnStart.setIcon(QtGui.QIcon(QtGui.QPixmap(":/icons/pause.png")))
            
            self.timer.start(1000)
            self.thread.start()
            
        elif self.status == "started":
            self.status = "paused"
            
            self.btnStart.setText("Продовжити")
            self.btnStart.setIcon(QtGui.QIcon(QtGui.QPixmap(":/icons/play.png")))
            
            self.handlePause()
    
    def handlePause(self):
        self.timer.stop()
    
    def handleStop(self):
        self.status = "stoped"
        
        self.disabledWhenStart(False)
        
        self.btnStart.setText("Старт обчислень")
        self.btnStart.setIcon(QtGui.QIcon(QtGui.QPixmap(":/icons/play.png")))
        
        if self.timer.isActive():
            self.timer.stop()
        if self.thread.isRunning():
            self.thread.quit()
        self.m.reset()

    def MetaTableReset(self):
        self.metaRows["name"].setText(self.currentTabText)
        self.metaRows["all"].setText("1")
        self.metaRows["complete"].setText("0")
        self.metaRows["progressBar"].setValue(0)
        self.metaRows["time"].setText("")
        self.metaRows["left"].setText("")
        #self.metaRows["result"].setText("")
        
        self.tableMetadata.resizeColumnsToContents()

    def MetaAllUpdate(self):
        self.m.All = self.currentTab.coreNumber(self.m.seq, self.m.K)
        self.metaRows["all"].setText( str(self.m.All) )
        self.tableMetadata.resizeColumnsToContents()
        
    def MetaTimeUpdate(self):
        self.metaRows["time"].setText( self.m.time )
        self.metaRows["left"].setText( self.m.left )   
        self.tableMetadata.resizeColumnsToContents()
        
    def MetaProgressUpdate(self, complete):
        self.metaRows["complete"].setText( str(complete) )
        self.tableMetadata.resizeColumnsToContents()
                
        
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
        

            
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    c = Controller()
    c.run()
