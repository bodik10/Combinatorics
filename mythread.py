from PySide import QtCore

from time import time


class MyThread(QtCore.QThread):
    def __init__(self, parent, func = None):
        QtCore.QThread.__init__(self, parent)
        self.c = parent
        self.func = func
        
    def run(self):
        seq = self.c.m.seq
        K = self.c.m.K
        
        start = time()
        
        for RES in self.func(seq, K):
            
            #self.c.m.result.append( str(RES) )                             # [('a', 'b', 'c'), ... ]
            self.c.m.result.append( "(" + ", ".join(map(str, RES)) + ")" )  # ('a', 'b', 'c') -> (a, b, c)
            self.c.m.complete += 1
            
            if len(self.c.m.result)>=50000 and len(self.c.m.result)%self.c.m.columns == 0:
                self.c.flushResult()
                
            percent = self.c.m.complete / self.c.m.All * 100
            
            if percent in range(0, 101, 5):     # update progress every 5%
                print(percent)
                """
                self.emit(QtCore.SIGNAL("upd_prog_bar(int)"), int(percent))
                self.emit(QtCore.SIGNAL("upd_prog(int)"), self.c.m.complete)"""
                
            if percent in range(5, 101, 25):    # update left time every 25%, starting at 5%
                print(percent)
                """
                delta = int(time() - start)
                approx_left = delta / percent * 100 
                
                print(approx_left)
                
                self.emit(QtCore.SIGNAL("upd_left_time(int)"), int(approx_left))
                
                start = time()
              """
            while self.c.status=="paused":
                self.msleep(500)
