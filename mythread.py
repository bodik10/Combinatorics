from PySide import QtCore

class MyThread(QtCore.QThread):
    def __init__(self, parent, func = None):
        QtCore.QThread.__init__(self, parent)
        self.c = parent
        self.func = func
        
    def run(self):
        seq = self.c.m.seq
        K = self.c.m.K
        
        for RES in self.func(seq, K):
            
            #self.c.m.result.append( str(RES) )                             # [('a', 'b', 'c'), ... ]
            self.c.m.result.append( "(" + ", ".join(map(str, RES)) + ")" )  # ('a', 'b', 'c') -> (a, b, c)
            self.c.m.complete += 1
            
            if len(self.c.m.result)>=50000 and len(self.c.m.result)%self.c.m.columns == 0:
                self.c.flushResult()
                
            while self.c.status=="paused":
                self.msleep(500)
