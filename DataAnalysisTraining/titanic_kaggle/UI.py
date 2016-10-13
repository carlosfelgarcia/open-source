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
        main_layout.setSpacing(200)
        
        # ---------------- Left UI --------------------------
        main_left_layout = qg.QVBoxLayout()
        main_left_layout.setContentsMargins(5, 5, 5, 5)
        main_left_layout.setSpacing(50)
        
        add_col_widget = qg.QWidget()
        add_col_widget.setFixedHeight(400)
        add_col_widget.setFixedWidth(450)
        add_col_layout = qg.QVBoxLayout()
        add_col_widget.setLayout(add_col_layout)
        add_col_widget.layout().setAlignment(qc.Qt.AlignTop)
        add_col_widget.layout().setSpacing(10)
        
        
        # Add column widgets
        # Font
        font = qg.QFont()
        font.setBold(True)
        font.setCapitalization(qg.QFont.Capitalize)
        font.setPixelSize(12)
        
        new_col_lb = qg.QLabel('Add new Column')
        new_col_lb.setFont(font)
        new_col_name_txt = qg.QLineEdit()
        new_col_name_txt.setMinimumWidth(400)
        new_col_name_txt.setPlaceholderText('Type New Column name ...')
        
        col_name1_lb = qg.QLabel('Column 1 Name')
        col_name1_lb.setFont(font)
        col_name1_txt = qg.QLineEdit()
        col_name1_txt.setPlaceholderText('Type Column name')
        
        col_name2_lb = qg.QLabel('Column 2 Name')
        col_name2_lb.setFont(font)
        col_name2_txt = qg.QLineEdit()
        col_name2_txt.setPlaceholderText('Type Column name')
        
        col_logic_lb = qg.QLabel('Logic')
        col_logic_lb.setFont(font)
        col_logic_txt = qg.QTextEdit()
        col_logic_txt.setText('Type the logic that relates the columns, e.g...'
                              '\ndef male_female_child(passenger):\n'
                              '    age,sex = passenger\n'
                              '    if age < 16:\n'
                              '        return "child"\n'
                              '    else:\n'
                              '        return sex')
        col_logic_txt.setMaximumHeight(150)
        
        new_col_btn = qg.QPushButton('Add Column')
        
        # Add widgets to column layout
        add_col_layout.addWidget(new_col_lb)
        add_col_layout.addWidget(new_col_name_txt)
        add_col_layout.addWidget(col_name1_lb)
        add_col_layout.addWidget(col_name1_txt)
        add_col_layout.addWidget(col_name2_lb)
        add_col_layout.addWidget(col_name2_txt)
        add_col_layout.addWidget(col_logic_lb)
        add_col_layout.addWidget(col_logic_txt)
        add_col_layout.addWidget(new_col_btn)
        
        # Button_layout
        btns_widget = qg.QWidget()
        btns_layout = qg.QHBoxLayout()
        btns_widget.setLayout(btns_layout)
        btns_layout.setSpacing(4)
        btns_layout.setAlignment(qc.Qt.AlignTop)
        btns_layout.addWidget(qg.QPushButton('Test'))
        
        main_left_layout.addWidget(add_col_widget)
        main_left_layout.addWidget(btns_widget)

        # ---------------- Right UI --------------------------
        
        # Table Layout
        table_layout = qg.QHBoxLayout()
        table_layout.setContentsMargins(5, 5, 5, 5)
        table_layout.setAlignment(qc.Qt.AlignTop)
        
        # Table widget
        columns = sorted(table.keys())
        table_w = qg.QTableWidget()
        pref_size = len(columns) * 106
        resize = False
        if pref_size < TABLE_SIZE:
            table_w.setMinimumWidth(pref_size)
        else:
            resize = True
            table_w.setMinimumWidth(TABLE_SIZE)
        
        table_w.setMinimumHeight(700)
        
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
                        if value == 'nan':
                            value = '---'
                    
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
        main_layout.addLayout(main_left_layout)
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