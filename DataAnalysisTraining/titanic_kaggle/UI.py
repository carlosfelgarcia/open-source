'''
Created on Oct 12, 2016

@author: Carlos Garcia
'''
# PyQt imports
import PyQt4.QtCore as qc
import PyQt4.QtGui as qg

# Built-in imports
import sys
import collections

# External libraries Imports
import numpy as np

# Core imports
import main

# Constants
TABLE_SIZE = 700


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
    def __init__(self, table):
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
        
        # Parent Info widget
        main_info_layout = qg.QVBoxLayout()
        main_info_layout.setContentsMargins(5, 5, 5, 5)
        main_info_layout.setSpacing(50)
        
        parent_info_widget = qg.QWidget()
        info_layout = qg.QVBoxLayout()
        parent_info_widget.setLayout(info_layout)
        parent_info_widget.layout().setContentsMargins(0, 0, 0, 0)
#         parent_info_widget.setSizePolicy(qg.QSizePolicy.Minimum,
#                                          qg.QSizePolicy.Minimum)
        
        # Info Layout
        columns = sorted(table.keys())
        num_columns = len(columns)
        info_layout.setSpacing(17)
        info_layout.setAlignment(qc.Qt.AlignTop)
        
        # Font
        font = qg.QFont()
        font.setBold(True)
        font.setCapitalization(qg.QFont.Capitalize)
        font.setPixelSize(16)
        
        # Data Columns
        self.columns_labels = []
        
        for col in columns:
            label_col = qg.QLabel()
            label_col.setFont(font)
            self.columns_labels.append(label_col)
            label_col.setText(col)
            info_layout.addWidget(label_col)
        # Just for testing
#         counter = 0
#         for col in self.columns_labels:
#             col.setText(str(counter))
#             counter += 1
        
        
        
        # Button_layout
        btns_widget = qg.QWidget()
        btns_layout = qg.QHBoxLayout()
        btns_widget.setLayout(btns_layout)
        btns_layout.setSpacing(4)
        btns_layout.setAlignment(qc.Qt.AlignTop)
        btns_layout.addWidget(qg.QPushButton('test'))
        
        main_info_layout.addWidget(parent_info_widget)
        main_info_layout.addWidget(btns_widget)

        
        # Table Layout
        table_layout = qg.QHBoxLayout()
        table_layout.setContentsMargins(5, 5, 5, 5)
        table_layout.setAlignment(qc.Qt.AlignTop)
        
        # Table widget
        table_w = qg.QTableWidget()
        pref_size = len(columns) * 106
        resize = False
        if pref_size < TABLE_SIZE:
            table_w.setFixedWidth(pref_size)
        else:
            resize = True
            table_w.setFixedWidth(TABLE_SIZE)
            table_w.setFixedHeight(700)
        
        # Add values to the table
        for column in columns:
            col_num = table_w.columnCount()
            row_total_num = table_w.rowCount()
            table_w.insertColumn(col_num)
            col_item = qg.QTableWidgetItem(column)
            table_w.setHorizontalHeaderItem(col_num, col_item)
            if isinstance(table[column], collections.Iterable):
                for i in xrange(len(table[column])):
                    value = ''
                    if isinstance(value, np.float64):
                        value = np.int(table[column][i])

                    elif isinstance(value, str):
                        value = str(table[column][i])
                    
                    table_item = qg.QTableWidgetItem(value)
                    
                    if i >= row_total_num:
                        table_w.insertRow(i)
                    table_w.setItem(i, col_num, table_item)
            else:
                table_w.insertRow(row_total_num)
                table_item = qg.QTableWidgetItem(table[column])
                table_w.setItem(row_total_num, col_num, table_item)
        
        if resize:
            table_w.resizeColumnsToContents()
            table_w.resizeRowsToContents()
        table_layout.addWidget(table_w)
        
        # Added Main Layout
        main_layout.addLayout(main_info_layout)
        main_layout.addLayout(table_layout)
        page1_widget.setLayout(main_layout)
        
        tab_widget.addTab(page1_widget, 'Tables')
        
        self.layout().addWidget(tab_widget)
    

def run():
    titanic = main.Main_Titanic()
    table = titanic.get_data('train.csv')
    app = qg.QApplication(sys.argv)
    
    main_ui = UI()
    dialog = main_dialog(table)
    main_ui.setCentralWidget(dialog)
    main_ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()