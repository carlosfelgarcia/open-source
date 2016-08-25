'''
Created on Aug 25, 2016

@author: User
'''

import PyQt4.QtCore as qc
import PyQt4.QtGui as qg
import sys


class Frame_test(qg.QDialog):
    def __init__(self):
        qg.QDialog.__init__(self)
        self.setWindowTitle("Testing UI")
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.setFixedHeight(350)
        self.setMinimumWidth(300)
        
        self.setLayout(qg.QVBoxLayout())
        self.layout().setContentsMargins(5, 5, 5, 5)
        
        # ---------------------------- Top --------------------------------
        top_frame = qg.QFrame()
        top_frame.setFrameStyle(qg.QFrame.Panel | qg.QFrame.Raised)
        
        # ---------------------------- Mid --------------------------------
        mid_frame = qg.QFrame()
        mid_frame.setFrameStyle(qg.QFrame.Panel | qg.QFrame.Raised)
        mid_frame.setLayout(qg.QHBoxLayout())
        
        mid_frame.layout().setContentsMargins(5, 5, 5, 5)
        mid_frame.layout().setSpacing(2)
        mid_frame.layout().setAlignment(qc.Qt.AlignTop)
        mid_frame.layout().addWidget(qg.QPushButton("Btn 1"))
        mid_frame.layout().addWidget(qg.QPushButton("Btn 2"))
        mid_frame.layout().addWidget(qg.QPushButton("Btn 3"))
        mid_frame.layout().addWidget(qg.QPushButton("Btn 4"))
        
        # ---------------------------- Low --------------------------------
        low_frame = qg.QFrame()
        low_frame.setFrameStyle(qg.QFrame.Panel | qg.QFrame.Raised)
        
        self.layout().addWidget(top_frame)
        self.layout().addWidget(mid_frame)
        self.layout().addWidget(low_frame)
        
        
def run():
    app = qg.QApplication(sys.argv)
    dialog = Frame_test()
    dialog.show()
    sys.exit(app.exec_())

run()
