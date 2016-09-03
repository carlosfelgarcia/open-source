'''
Created on Sep 2, 2016

@author: co2_k
'''


import PyQt4.QtGui as qg
import PyQt4.QtCore as qc
import sys


# ----------------------------- UI ---------------------------------------
class Frame(qg.QDialog):
    def __init__(self):
        qg.QDialog.__init__(self)
        self.setWindowTitle('Interpolate it')
        self.setFixedHeight(150)
        self.setFixedWidth(400)
        
        self.setLayout(qg.QVBoxLayout())
        self.layout().setAlignment(qc.Qt.AlignTop)
        self.layout().setContentsMargins(5, 5, 5, 5)
        self.layout().setSpacing(5)
        
#         title_layout = qg.QHBoxLayout()
#         title_txt = qg.QLineEdit('Untitled')
#         self.exit_btn = qg.QPushButton('X')
#         self.exit_btn.setFixedWidth(40)
#         title_layout.addWidget(title_txt)
#         title_layout.addWidget(self.exit_btn)
#         self.layout().addLayout(title_layout)
        
        buttons_1_layout = qg.QHBoxLayout()
        self.store_btn = qg.QPushButton('Store Items')
        self.clean_btn = qg.QPushButton('Clear Items')
        buttons_1_layout.addSpacerItem(qg.QSpacerItem(5, 5, qg.QSizePolicy.Expanding))
        buttons_1_layout.addWidget(self.store_btn)
        buttons_1_layout.addWidget(self.clean_btn)
        buttons_1_layout.addSpacerItem(qg.QSpacerItem(5, 5, qg.QSizePolicy.Expanding))
        self.layout().addLayout(buttons_1_layout)
        
        buttons_2_layout = qg.QHBoxLayout()
        self.start_btn = qg.QPushButton('Store Start')
        self.reset_btn = qg.QPushButton('Reset')
        self.end_btn = qg.QPushButton('Store Ends')
        buttons_2_layout.addWidget(self.start_btn)
        buttons_2_layout.addWidget(self.reset_btn)
        buttons_2_layout.addWidget(self.end_btn)
        self.layout().addLayout(buttons_2_layout)
        
        slider_layout = qg.QHBoxLayout()
        slider_start_lb = qg.QLabel('Start')
        slider = qg.QSlider(qc.Qt.Horizontal)
        slider_end_lb = qg.QLabel('End')
        slider_layout.addWidget(slider_start_lb)
        slider_layout.addWidget(slider)
        slider_layout.addWidget(slider_end_lb)
        self.layout().addLayout(slider_layout)
        
        check_layout = qg.QHBoxLayout()
        self.trans_chk = qg.QCheckBox('Transform')
        self.attrs_chk = qg.QCheckBox('UD Attributes')
        self.attrs_chk.setCheckState(qc.Qt.Checked)
        check_layout.addWidget(self.trans_chk)
        check_layout.addSpacerItem(qg.QSpacerItem(5, 5, qg.QSizePolicy.Expanding))
        check_layout.addWidget(self.attrs_chk)
        self.layout().addLayout(check_layout)
        

def run():
    app = qg.QApplication(sys.argv)
    dialog = Frame()
    dialog.show()
    sys.exit(app.exec_())

run()