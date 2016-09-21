'''
Created on Sep 20, 2016

@author: Carlos Garcia
'''
# PyQt imports
import PyQt4.QtCore as qc
import PyQt4.QtGui as qg

# Built-in imports
import sys


class UI(qg.QMainWindow):
    '''
    Main UI
    '''

    def __init__(self):
        '''
        Constructor
        '''
        # Variables
        self.file_actions = []
        
        # Main Window
        qg.QMainWindow.__init__(self)
        self.setWindowTitle('UI Test')
        pos = qg.QApplication.desktop().cursor().pos()
        screen = qg.QApplication.desktop().screenNumber(pos)
        centerPoint = qg.QApplication.desktop().screenGeometry(screen).center()
        self.setGeometry(centerPoint.x() / 2, centerPoint.y() / 2, 1020, 720)
        
        # Add menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        
        # Add file actions
        self.add_file_actions()
        for action in self.file_actions:
            file_menu.addAction(action)
        
    def add_file_actions(self):
        '''
        Added the file actions to a pre-existing list
        '''
        quit_action = qg.QAction("&Quit", self)
        quit_action.setShortcut("Ctrl+Q")
        quit_action.setStatusTip("Quit the app")
        
        open_action = qg.QAction("&Open File", self)
        open_action.setShortcut("Ctrl+O")
        open_action.setStatusTip("Open File")
        
        # Connections
        quit_action.triggered.connect(self.close_window)
        open_action.triggered.connect(self.open_file)
        
        # Add Actions to the list
        self.file_actions.append(quit_action)
        self.file_actions.append(open_action)
        
    def close_window(self):
        # TODO
        print 'close'
        
    def open_file(self):
        # TODO
        print 'open'


class main_dialog(qg.QDialog):
    '''
    This is the main dialog
    '''
    def __init__(self):
        qg.QDialog.__init__(self)
        
        self.setLayout(qg.QHBoxLayout())
        self.layout().setContentsMargins(5, 5, 5, 5)
        self.layout().setSpacing(2)
        
        # Tab Widget
        tab_widget = qg.QTabWidget()
        tab_widget.setTabPosition(0)
        
        # Widget for tab1
        page1_widget = qg.QWidget()
        
        # Main Layout
        main_layout = qg.QHBoxLayout()
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(2)
        
        # Info Layout
        info_layout = qg.QVBoxLayout()
        info_layout.setContentsMargins(5, 30, 5, 5)
        info_layout.setSpacing(30)
        info_layout.setAlignment(qc.Qt.AlignTop)
        
        label_col1 = qg.QLabel()
        self._text_col1 = ''
        label_col1.setText('Column 1: %s' % self._text_col1)
        
        label_col2 = qg.QLabel()
        self._text_col2 = ''
        label_col2.setText('Column 2: %s' % self._text_col2)
        
        label_col3 = qg.QLabel()
        self._text_col3 = ''
        label_col3.setText('Column 3: %s' % self._text_col3)
        
        info_layout.addWidget(label_col1)
        info_layout.addWidget(label_col2)
        info_layout.addWidget(label_col3)
        # Button_layout
        
        # Table Layout
        
        
        # Added Main Layout
        main_layout.addLayout(info_layout)
        page1_widget.setLayout(main_layout)
        
        tab_widget.addTab(page1_widget, 'Tables')
        
        self.layout().addWidget(tab_widget)
    

def run():
    app = qg.QApplication(sys.argv)
    
    main_ui = UI()
    dialog = main_dialog()
    main_ui.setCentralWidget(dialog)
    main_ui.show()
    sys.exit(app.exec_())

run()
