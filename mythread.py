from PySide import QtCore

class MyThread(QtCore.QThread):
    def __init__(self, parent):
        QtCore.QThread.__init__(self, parent)
        self.c = parent
        
    def run(self):
        for RES in self.c.currentTab.coreGenerator(self.c.m.seq, self.c.m.K):
            self.c.m.result.append(RES)
            self.c.m.complete += 1
            
            #self.emit(QtCore.SIGNAL("upd_prog_bar(int)"), round(self.c.m.complete / self.c.m.All * 100))
            #self.emit(QtCore.SIGNAL("upd_prog(int)"), self.c.m.complete)
            
            while self.c.status=="paused":
                self.msleep(500)
