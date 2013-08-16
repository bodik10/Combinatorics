from PySide import QtCore

class MyTimer(QtCore.QTimer):
    '''
    classdocs
    '''
    
    def __init__(self, parent):
        '''
        Constructor
        '''
        QtCore.QTimer.__init__(self, parent)
        self.c = parent
        
        self.connect(self, QtCore.SIGNAL("timeout()"), self.update_time);
        
    def update_left(self, left):
        if left<60:
            unit = "сек."
            val = left
        elif 60<=left<3600:
            unit = "хв."
            val = left//60
        elif 3600<=left<86400:
            unit = "год. (приблизно)"
            val = round(left/3600)
        elif left>=86400:
            unit = "дн. (приблизно)"
            val = round(left/86400)
            
        self.c.m.left = "%s %s" % (val, unit)
                
    def update_time(self):
        self.c.m.time_sec += 1
        
        time = self.c.m.time_sec
        self.c.m.time = "{0:02d}:{1:02d}:{2:02d}".format( *(time//3600, (time//60)%60, time%60) )
        
        self.c.m.left_sec -= 1
        self.update_left(self.c.m.left_sec)
        self.c.MetaTimeUpdate()
