'''
Created on Aug 25, 2016

@author: User
'''

import PyQt4.QtCore as qc
import PyQt4.QtGui as qg
import sys


class UI_test2(qg.QDialog):
    def __init__(self):
        qg.QDialog.__init__(self)
        self.setWindowTitle("Testing UI")
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.setFixedHeight(350)
        self.setFixedWidth(300)
        
        self.setLayout(qg.QVBoxLayout())
        stack_layout = qg.QStackedLayout()
        self.layout().addLayout(stack_layout)
         
        main_btns_lay = qg.QHBoxLayout()
        main_btns_lay.addWidget(qg.QPushButton("Layout 1"))
        main_btns_lay.addWidget(qg.QPushButton("Layout 2"))
        main_btns_lay.addWidget(qg.QPushButton("Layout 3"))
        main_btns_lay.addWidget(qg.QPushButton("Layout 4"))
         
        self.layout().addLayout(main_btns_lay)
        
        widget1 = qg.QWidget()
        widget1.setLayout(qg.QVBoxLayout())
        widget1.layout().addWidget(qg.QPushButton("Btn 1"))
        widget1.layout().addWidget(qg.QPushButton("Btn 2"))
        widget1.layout().addWidget(qg.QPushButton("Btn 3"))
        widget1.layout().addWidget(qg.QPushButton("Btn 4"))
        
        stack_layout.addWidget(widget1)

def run():
    app = qg.QApplication(sys.argv)
    dialog = UI_test2()
    dialog.show()
    sys.exit(app.exec_())

run()

