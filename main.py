'''
Created on 1 серп. 2013

@author: Бодя
'''

import sys, os

from view import View
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
        self.metaRows["result"].setText(os.path.abspath(self.m.file.name))
        self.tableMetadata.resizeColumnsToContents()

        self.show()
    
    def run(self):
        sys.exit(app.exec_())
        
    def closeEvent(self, event):    # clean garbage
        if self.status in ["started", "paused"]:
            self.handleStop()       # stop thread    
        del self.m                  # close file
        event.accept()     

    def handleEvents(self):
        # enable/disable spinBox or plainTextEdit
        self.connect(self.radioN, QtCore.SIGNAL("toggled(bool)"), self.spinN.setEnabled)
        self.connect(self.radioNCustom, QtCore.SIGNAL("toggled(bool)"), self.plainNCustom.setEnabled)

        self.tabComb.currentChanged.connect(self.handleChangeTab)
        
        # link in QLabel leads to other Tab within QTabWidget
        self.label.linkActivated.connect(lambda link: self.tabComb.setCurrentIndex(int(link[4:])))

        # prevent setting K larger than N
        # self.spinN.valueChanged.connect(lambda value: self.spinK.setMaximum(value))


        self.spinColumns.valueChanged["int"].connect(lambda val: setattr(self.m, "columns", val))
        
        self.tabComb.currentChanged.connect(self.handleChange)
        self.plainNCustom.textChanged.connect(self.handleChange)
        self.spinN.valueChanged.connect(self.handleChange)
        self.spinK.valueChanged.connect(self.handleChange)
        self.radioN.clicked.connect(self.handleChange)
        self.radioNCustom.clicked.connect(self.handleChange)
        
        self.btnStart.clicked.connect(self.handleStart)
        self.btnStop.clicked.connect(self.handleStop)
        self.btnResultPath.clicked.connect(self.handleChangePath)
        self.metaRows["btnClear"].clicked.connect(self.handleClearResult)
        
        self.tableMetadata.cellDoubleClicked.connect(self.openResult)
        
        self.connect(self.timer, QtCore.SIGNAL("upd_prog_bar(int)"), self.metaRows["progressBar"], QtCore.SLOT("setValue(int)"))
        self.thread.finished.connect(self.handleStop)

    def handleChange(self):
        if self.plainNCustom.isEnabled():
            self.m.seq = self.plainNCustom.toPlainText().split()
            if not self.m.seq: return
            #self.spinK.setMaximum(len(self.m.seq)) # if k can't be larger than N
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
        disableList = [self.tabComb, self.groupInput, self.checkMetadata, self.checkShowResult, self.spinColumns, self.btnResultPath, self.metaRows["btnClear"]]
        
        self.btnStop.setEnabled(flag)
        
        for w in disableList:
            w.setDisabled(flag)
        
    def handleStart(self):
        if self.status in ["stoped", "paused"]:
            if self.status == "stoped":
                self.writeMetaData()
            
            self.status = "started"
            
            self.disabledWhenStart(True)
            self.btnStart.setText("Призупинити")
            self.btnStart.setIcon(QtGui.QIcon(QtGui.QPixmap(":/icons/pause.png")))
            
            self.timer.start(1000)
            self.thread.func = self.currentTab.coreGenerator
            self.thread.start()
            
        elif self.status == "started":
            self.status = "paused"
            
            self.btnStart.setText("Продовжити")
            self.btnStart.setIcon(QtGui.QIcon(QtGui.QPixmap(":/icons/play.png")))
            
            self.handlePause()
    
    def handlePause(self):
        self.timer.stop()
        if self.checkShowResult.isChecked():
            self.openResult()
    
    def handleStop(self):
        self.status = "stoped"
        
        self.disabledWhenStart(False)
        
        self.btnStart.setText("Старт обчислень")
        self.btnStart.setIcon(QtGui.QIcon(QtGui.QPixmap(":/icons/play.png")))
        
        if self.timer.isActive():
            self.timer.stop()
            self.MetaTimeUpdate() # adjustment meta data
            
        self.flushResult()
      
        if self.checkShowResult.isChecked():
            self.openResult()
        
        self.m.reset()

    def handleChangePath(self):
        path = QtGui.QFileDialog.getSaveFileName(parent=self, caption="Виберіть новий файл, для збереження результату", 
                                                 directory=QtCore.QDir.currentPath(), filter="Text files (*.txt)")
        if path[0]:
            self.m.filename = path[0]
            self.m.file.close()
            self.m.file = open(os.path.normpath(self.m.filename), "w+", encoding="utf8")
            self.metaRows["result"].setText(os.path.abspath(self.m.file.name))
            self.tableMetadata.resizeColumnsToContents()  
                  
    def handleClearResult(self):
        self.m.file.close()
        self.m.file = open(self.m.filename, "w+", encoding="utf-8")
        self.metaRows["labelSize"].setText("0 байт")
        
    # periodically write data from result list to file
    def flushResult(self):
        i=0
        columns = self.m.columns
        result = ""
        while i<len(self.m.result):
            result += "\t".join(self.m.result[i : (i+columns)]) + "\n"
            i += columns
        
        self.m.file.write(result)
        self.m.file.flush()
        self.MetaFileSizeUpdate()
        
        self.m.result = []
           
    def openResult(self, row=6, col=0): # row and col here recieves from table's cell dblClick signal
        if row==6 and col==0:
            os.startfile(os.path.abspath(self.m.file.name))
            # os.popen("notepad " + os.path.abspath(self.m.file.name))     # could be that variant as well
            
    def writeMetaData(self):
        if self.checkMetadata.isChecked():
            meta = "{0}\n{0}\n\nТип: {1}\nВхідні дані: N={2}{3}\nВсього комбінацій: {4}\n{0}\n".format(
                "-"*40, 
                self.currentTabText,
                len(self.m.seq),
                ", k=%s" % self.spinK.value() if self.tabComb.currentIndex != 4 else "",
                self.m.All
            )
            
            self.m.file.write(meta)
            self.m.file.flush()
            
   
    def MetaTableReset(self):
        self.metaRows["name"].setText(self.currentTabText)
        self.metaRows["all"].setText("1")
        self.metaRows["complete"].setText("0")
        self.metaRows["progressBar"].setValue(0)
        self.metaRows["time"].setText("")
        self.metaRows["left"].setText("")
        self.tableMetadata.resizeColumnsToContents()

    def MetaAllUpdate(self):
        try:
            self.m.All = self.currentTab.coreNumber(self.m.seq, self.m.K)
        except ValueError:
            self.m.All = 0
        self.metaRows["all"].setText( str(self.m.All) )
        self.tableMetadata.resizeColumnsToContents()
        
    def MetaTimeUpdate(self):
        self.metaRows["time"].setText( self.m.time )
        self.metaRows["left"].setText( self.m.left )
        self.metaRows["complete"].setText( str(self.m.complete) )
        
        self.tableMetadata.resizeColumnsToContents()
               
    def MetaFileSizeUpdate(self):
        size = os.stat(os.path.abspath(self.m.filename)).st_size # get size of the file in bytes
        l_size = list(str(size))
        for i in range(len(l_size)-3, 0, -3):   # insert space in each 3rd position from the end
            l_size.insert(i, " ")               # 12345678 -> 12 345 678
            
        self.metaRows["labelSize"].setText("".join(l_size)  + " байт" ) 
        
        
class ModelMetadata:
    def __init__(self):
        self.seq = [1]
        self.K = self.All = self.complete = 0
        
        self.time_sec = 0
        self.left_sec = 0 
        self.left = self.time = ""
        
        self.columns = 1
        self.result = []
        
        self.filename = "result.txt"
        self.file = open(self.filename, "w+", encoding="utf-8")
        
    def reset(self):
        self.result = []
        self.complete = 0
        self.time_sec = 0
        self.left_sec = 0 
        self.left = self.time = ""
        
    def __del__(self):
        self.file.close()
        
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    c = Controller()
    c.run()
