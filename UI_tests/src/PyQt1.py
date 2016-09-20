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
        

class UI_Text_Btn(qg.QDialog):
    def __init__(self):
        qg.QDialog.__init__(self)
        self.setWindowTitle("Testing UI")
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.setFixedHeight(350)
        self.setMinimumWidth(300)
        
        self.setLayout(qg.QVBoxLayout())
        self.layout().setSpacing(5)
        
        text_layout = qg.QHBoxLayout()
        text_layout.setSpacing(5)
        
        text_lb = qg.QLabel('Example: ')
        font_lb = qg.QFont()
        font_lb.setItalic(True)
        text_lb.setFont(font_lb)
        text_layout.addWidget(text_lb)
        
        txt_field = qg.QLineEdit()
        txt_field.setPlaceholderText('Type here...')
        
        regex = qc.QRegExp('[0-9]+')
        validator = qg.QRegExpValidator(regex, txt_field)
        txt_field.setValidator(validator)
        text_layout.addWidget(txt_field)
        
        self.txt_editor = qg.QTextEdit()
        self.txt_editor.setWordWrapMode(qg.QTextOption.ManualWrap)
        text_layout.addWidget(self.txt_editor)
        
        btn_layout = qg.QHBoxLayout()
        btn_layout.setSpacing(5)
        
        btn_ex = qg.QPushButton("Button")
        btn_layout.addWidget(btn_ex)
        
        radio_btn_a = qg.QRadioButton('a')
        radio_btn_b = qg.QRadioButton('b')
        radio_btn_c = qg.QRadioButton('c')
        radio_btn_d = qg.QRadioButton('d')
        
        btn_group_1 = qg.QButtonGroup(self)
        btn_group_2 = qg.QButtonGroup(self)
        
        btn_group_1.addButton(radio_btn_a)
        btn_group_1.addButton(radio_btn_b)
        btn_group_2.addButton(radio_btn_c)
        btn_group_2.addButton(radio_btn_d)
        
        btn_layout.addWidget(radio_btn_a)
        btn_layout.addWidget(radio_btn_b)
        btn_layout.addWidget(radio_btn_c)
        btn_layout.addWidget(radio_btn_d)
        
        btn_check = qg.QCheckBox("check")
        btn_layout.addWidget(btn_check)
        
        slide_layout = qg.QHBoxLayout()
        slide_layout.setSpacing(5)
        
        slide = qg.QSlider()
        slide.setOrientation(qc.Qt.Horizontal)
        slide_count = qg.QSpinBox()
        
        slide_layout.addWidget(slide)
        slide_layout.addWidget(slide_count)
        
        self.layout().addLayout(text_layout)
        self.layout().addLayout(btn_layout)
        self.layout().addLayout(slide_layout)
        
        slide.valueChanged.connect(slide_count.setValue)
        slide_count.valueChanged.connect(slide.setValue)
        
        btn_group_1.buttonClicked.connect(self.add_text)
        
    def add_text(self, button):
        self.txt_editor.setPlainText(self.txt_editor.toPlainText() +
                                     button.text())


def run():
    app = qg.QApplication(sys.argv)
    dialog = UI_Text_Btn()
    dialog.show()
    sys.exit(app.exec_())

run()
