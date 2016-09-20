'''
Created on Aug 31, 2016

@author: User
'''

import PyQt4.QtCore as qc
import PyQt4.QtGui as qg
import sys


# ------------------------------ Start UI ---------------------------------
class MainUI(qg.QDialog):
    def __init__(self):
        qg.QDialog.__init__(self)
        self.setWindowTitle("Main UI")
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setFixedHeight(400)
        self.setFixedWidth(450)
        
        self.setLayout(qg.QVBoxLayout())
        self.layout().setAlignment(qc.Qt.AlignTop)
        
        rename_widget = qg.QWidget()
        rename_widget.setLayout(qg.QVBoxLayout())
        rename_widget.setContentsMargins(2, 0, 2, 0)
        rename_widget.layout().setSpacing(10)
                
        name_layout = qg.QHBoxLayout()
        
        line_splitter = _Splitter('RENAME')
        rename_widget.layout().addWidget(line_splitter)
        
        name_layout.addWidget(qg.QLabel('New Name:'))
        self.name_field = qg.QLineEdit()
        reg_ex = qc.QRegExp("^(?!^_)[a-zA-Z_]+")
        text_validator = qg.QRegExpValidator(reg_ex, self.name_field)
        self.name_field.setValidator(text_validator)
        name_layout.addWidget(self.name_field)
        rename_widget.layout().addLayout(name_layout)
        
        rename_widget.layout().addLayout(_LineLayout())
        
        name_method_layout = qg.QHBoxLayout()
        name_method_layout.addWidget(qg.QLabel('Multiples Naming Method:'))
        self.combo_box = qg.QComboBox()
        self.combo_box.addItems(['Numbers (0-9)', 'Letters(a-z)'])
        self.combo_box.setFixedWidth(100)
        name_method_layout.addWidget(self.combo_box)
        rename_widget.layout().addLayout(name_method_layout)
        
        option_layout = qg.QHBoxLayout()
        self.padding_lb = qg.QLabel('No. Padding:')
        self.spin_box = qg.QSpinBox()
        self.spin_box.setRange(0, 10)
        self.spin_box.setFixedWidth(40)
        self.lower_btn = qg.QRadioButton('Lowercase')
        self.upper_btn = qg.QRadioButton('Uppercase')
        self.lower_btn.setVisible(False)
        self.upper_btn.setVisible(False)
        self.lower_btn.setChecked(True)
        spacer_item = qg.QSpacerItem(5, 5, qg.QSizePolicy.Expanding)
        option_layout.addWidget(self.padding_lb)
        option_layout.addWidget(self.lower_btn)
        option_layout.addSpacerItem(spacer_item)
        option_layout.addWidget(self.spin_box)
        option_layout.addWidget(self.upper_btn)
        rename_widget.layout().addLayout(option_layout)
        
        rename_widget.layout().addLayout(_LineLayout())
        
        pre_suf_layout = qg.QHBoxLayout()
        self.pre_check = qg.QCheckBox('Prefix:')
        self.pre_text = qg.QLineEdit()
        self.pre_text.setValidator(text_validator)
        self.pre_text.setEnabled(False)
        self.suf_check = qg.QCheckBox('Suffix:')
        self.suf_text = qg.QLineEdit()
        self.suf_text.setValidator(text_validator)
        self.suf_text.setEnabled(False)
        pre_suf_layout.addWidget(self.pre_check)
        pre_suf_layout.addWidget(self.pre_text)
        line = qg.QFrame()
        line.setFrameStyle(qg.QFrame.VLine)
        line.setFixedWidth(30)
        pre_suf_layout.addWidget(line)
        pre_suf_layout.addWidget(self.suf_check)
        pre_suf_layout.addWidget(self.suf_text)
        rename_widget.layout().addLayout(pre_suf_layout)
        
        example_layout = qg.QHBoxLayout()
        self.example_lb = qg.QLabel('e.g.')
        self.example_btn = qg.QPushButton('Rename')
        self.example_btn.setFixedWidth(100)
        example_layout.addWidget(self.example_lb)
        example_layout.addWidget(self.example_btn)
        rename_widget.layout().addLayout(example_layout)
        
        self.layout().addWidget(rename_widget)
        
# ------------------------------ Connections ---------------------------------
        self.combo_box.currentIndexChanged.connect(self._ChangeVisibility)
        
        self.pre_check.stateChanged.connect(self.pre_text.setEnabled)
        self.suf_check.stateChanged.connect(self.suf_text.setEnabled)
        
        self.name_field.textChanged.connect(self._update_label)
        self.spin_box.valueChanged.connect(self._update_label)
        self.lower_btn.clicked.connect(self._update_label)
        self.upper_btn.clicked.connect(self._update_label)
        self.pre_text.textChanged.connect(self._update_label)
        self.suf_text.textChanged.connect(self._update_label)
        
        self.example_btn.clicked.connect(self._to_world)
        

# ------------------------------ Methods ---------------------------------
    def _ChangeVisibility(self, index):
        self.lower_btn.setVisible(index)
        self.upper_btn.setVisible(index)
        self.padding_lb.setVisible(not(index))
        self.spin_box.setVisible(not(index))
        self._update_label()
        
    def _update_label(self):
        # Get values
        padding = 0
        lower = True
        final_name = 'e.g. '
        
        if self.pre_check.isChecked():
            preffix = str(self.pre_text.text()).strip()
            final_name += preffix + '_'
            
        namefield = str(self.name_field.text()).strip()
        final_name += namefield + '_'
        
        index = self.combo_box.currentIndex()
        if index:
            lower = self.lower_btn.isChecked()
            if lower:
                final_name += 'a'
            else:
                final_name += 'A'
        else:
            padding = self.spin_box.value()
            final_name += ('0' * padding) + '1'

        if self.suf_check.isChecked():
            suffix = str(self.suf_text.text()).strip()
            final_name += '_' + suffix
            
        self.example_lb.setText(final_name)
        
    def _to_world(self):
        print "Going to the World"


# ------------------------------ Classes ---------------------------------
class _Splitter(qg.QWidget):
    def __init__(self, text='', color='#9C9C9C', shadow=True, size='1px'):
        qg.QWidget.__init__(self)
        self.setMinimumHeight(1)
        self.setLayout(qg.QHBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.layout().setAlignment(qc.Qt.AlignVCenter)
        
        line = qg.QFrame()
        line.setFrameStyle(qg.QFrame.HLine)
        
        shadow_style = ''
        if shadow:
            shadow_style = 'border-bottom: 1px solid #888888;'
        style_sheet = 'border: 0.5px solid #000000; \
                       background-color: %s; \
                       max-height: %s; \
                       %s ' % (color, size, shadow_style)
        
        line.setStyleSheet(style_sheet)
        self.layout().addWidget(line)
        
        if not text:
            return
        
        line.setFixedWidth(5)
        
        text_label = qg.QLabel(text)
        font = qg.QFont()
        font.setBold(True)
        
        text_width = qg.QFontMetrics(font).width(text) + 6
        text_label.setFont(font)
        
        text_label.setMaximumWidth(text_width)
        text_label.setAlignment(qc.Qt.AlignHCenter | qc.Qt.AlignVCenter)
        
        self.layout().addWidget(text_label)
        
        line_2 = qg.QFrame()
        line_2.setFrameStyle(qg.QFrame.HLine)
        line_2.setStyleSheet(style_sheet)
        self.layout().addWidget(line_2)
        
        
class _LineLayout(qg.QHBoxLayout):
        def __init__(self):
            qg.QHBoxLayout.__init__(self)
            self.setContentsMargins(8, 2, 8, 1)
            
            splitter = _Splitter(shadow=True, color='#808080', size='0.5px')
            splitter.setFixedHeight(1)
            
            self.addWidget(splitter)
            
            
# ------------------------------ Run ---------------------------------
def run():
    app = qg.QApplication(sys.argv)
    dialog = MainUI()
    dialog.show()
    sys.exit(app.exec_())

run()
