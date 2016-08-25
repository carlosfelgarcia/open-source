'''
Created on Aug 25, 2016

@author: User
'''

import PyQt4.QtCore as qc
import PyQt4.QtGui as qg
import sys
from functools import partial


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
        main_btn_1 = qg.QPushButton("Layout 1")
        main_btn_2 = qg.QPushButton("Layout 2")
        main_btn_3 = qg.QPushButton("Layout 3")
        main_btn_4 = qg.QPushButton("Layout 4")
        main_btns_lay.addWidget(main_btn_1)
        main_btns_lay.addWidget(main_btn_2)
        main_btns_lay.addWidget(main_btn_3)
        main_btns_lay.addWidget(main_btn_4)
         
        self.layout().addLayout(main_btns_lay)
        
        # ---------------Widget 1-----------------------------
        widget1 = qg.QWidget()
        widget1.setLayout(qg.QVBoxLayout())
        widget1.layout().addWidget(qg.QPushButton("Btn 1"))
        widget1.layout().addWidget(qg.QPushButton("Btn 2"))
        widget1.layout().addWidget(qg.QPushButton("Btn 3"))
        widget1.layout().addWidget(qg.QPushButton("Btn 4"))
        
        # ---------------Widget 2-----------------------------
        widget2 = qg.QWidget()
        widget2.setLayout(qg.QHBoxLayout())
        widget2.layout().addWidget(qg.QPushButton("Btn 1"))
        widget2.layout().addWidget(qg.QPushButton("Btn 2"))
        widget2.layout().addWidget(qg.QPushButton("Btn 3"))
        widget2.layout().addWidget(qg.QPushButton("Btn 4"))
        
        # ---------------Widget 3-----------------------------
        widget3 = qg.QWidget()
        widget3.setLayout(qg.QFormLayout())
        widget3.layout().addRow("Name :",qg.QLineEdit())
        widget3.layout().addRow("Tel :",qg.QLineEdit())
        widget3.layout().addRow("Age :",qg.QSpinBox())
        
        # ---------------Widget 4-----------------------------
        widget4 = qg.QWidget()
        widget4.setLayout(qg.QGridLayout())
        font_name = qg.QLabel("Font")
        font_style = qg.QLabel("Style")
        font_size = qg.QLabel("Size")
        
        font_name_list = qg.QListWidget()
        font_style_list = qg.QListWidget()
        font_size_list = qg.QListWidget()
        
        names = ["Times", "Helvetica", "Courier"]
        styles = ["Roman", "Italic", "Oblique"]
        sizes = [str(size) for size in range(10, 30, 2)]
        
        font_name_list.addItems(names)
        font_size_list.addItems(sizes)
        font_style_list.addItems(styles)
        
        widget4.layout().addWidget(font_name, 0, 0)
        widget4.layout().addWidget(font_name_list, 1, 0)
        widget4.layout().addWidget(font_style, 0, 1)
        widget4.layout().addWidget(font_style_list, 1, 1)
        widget4.layout().addWidget(font_size, 0, 2)
        widget4.layout().addWidget(font_size_list, 1, 2)
        
        # ----------------- End widgets -----------------------
        stack_layout.addWidget(widget1)
        stack_layout.addWidget(widget2)
        stack_layout.addWidget(widget3)
        stack_layout.addWidget(widget4)
        
        main_btn_1.clicked.connect(partial(stack_layout.setCurrentIndex, 0))
        main_btn_2.clicked.connect(partial(stack_layout.setCurrentIndex, 1))
        main_btn_3.clicked.connect(partial(stack_layout.setCurrentIndex, 2))
        main_btn_4.clicked.connect(partial(stack_layout.setCurrentIndex, 3))


def run():
    app = qg.QApplication(sys.argv)
    dialog = UI_test2()
    dialog.show()
    sys.exit(app.exec_())

run()

