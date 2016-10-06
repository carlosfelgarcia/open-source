'''
Created on Sep 20, 2016

@author: Carlos Garcia
'''
# PyQt imports
import PyQt4.QtCore as qc
import PyQt4.QtGui as qg

# Built-in imports
import sys
import collections

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
        
        # Info Layout
        columns = sorted(table.keys())
        num_columns = len(columns)
        info_layout = qg.QVBoxLayout()
        info_layout.setContentsMargins(5, 50, 5, 5)
        info_layout.setSpacing(10 * num_columns)
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
        
        # Add values to the table
        for column in columns:
            col_num = table_w.columnCount()
            row_total_num = table_w.rowCount()
            table_w.insertColumn(col_num)
            
            if isinstance(table[column], collections.Iterable):
                for i in xrange(len(table[column])):
                    table_item = qg.QTableWidgetItem(table[column][i])
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
        main_layout.addLayout(info_layout)
        main_layout.addLayout(table_layout)
        page1_widget.setLayout(main_layout)
        
        tab_widget.addTab(page1_widget, 'Tables')
        
        self.layout().addWidget(tab_widget)
    

def run():
    # Test data
    table = {'Column 1': ['A', 'BY', 'C'], 'Column 2': ['DW', 'E', 'F'],
             'Column 3': ['G', 'H', 'LI'], 'Column 4': ['G', 'H', 'LI']}
    
    app = qg.QApplication(sys.argv)
    
    main_ui = UI()
    dialog = main_dialog(table)
    main_ui.setCentralWidget(dialog)
    main_ui.show()
    sys.exit(app.exec_())

run()