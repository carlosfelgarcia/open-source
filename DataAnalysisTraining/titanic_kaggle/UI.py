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
import ctypes

# External libraries Imports
import numpy as np

# Core imports
import main_titanic

# Constants
TABLE_SIZE = 700


class MainWindow(qg.QMainWindow):
    '''
    MainWindow
    '''

    def __init__(self):
        '''
        Constructor
        '''
        # Variables
        self.file_actions = []
        
        # Main Window
        qg.QMainWindow.__init__(self)
        self.setWindowTitle('MainWindow Test')
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
        quit_action.triggered.connect(self._close_window)
        open_action.triggered.connect(self._open_file)
        
        # Add Actions to the list
        self.file_actions.append(quit_action)
        self.file_actions.append(open_action)
        
    def _close_window(self):
        # TODO
        print 'close'
        
    def _open_file(self):
        # TODO
        print 'open'


class MainDialog(qg.QDialog):
    '''
    This is the main dialog
    '''
    def __init__(self, titanic):
        qg.QDialog.__init__(self)
        
        # World instance
        self._titanic = titanic
        table = self._titanic.get_data('train.csv')
        
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
        main_layout.setSpacing(100)
        
        # ---------------- Left Side UI --------------------------
        main_left_layout = qg.QVBoxLayout()
        main_left_layout.setContentsMargins(5, 5, 5, 5)
        main_left_layout.setSpacing(50)
        
        add_col_widget = qg.QWidget()
        add_col_widget.setFixedHeight(500)
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
        self._txt_new_col_name = qg.QLineEdit()
        self._txt_new_col_name.setMinimumWidth(400)
        
        col_name1_lb = qg.QLabel('Column 1 Name')
        col_name1_lb.setFont(font)
        self._txt_col_name1 = qg.QLineEdit()
        
        col_name2_lb = qg.QLabel('Column 2 Name')
        col_name2_lb.setFont(font)
        self._txt_col_name2 = qg.QLineEdit()
        
        col_funct_name_lb = qg.QLabel('Fuction name')
        col_funct_name_lb.setFont(font)
        self._clean_txt = 0
        self._txt_col_funct_name = qg.QLineEdit()
        reg_ex = qc.QRegExp("[a-z0-9]+")
        text_validator = qg.QRegExpValidator(reg_ex, self._txt_col_funct_name)
        self._txt_col_funct_name.setValidator(text_validator)
        col_function_lb = qg.QLabel('Function')
        col_function_lb.setFont(font)
        self._txt_col_function = qg.QTextEdit()
        self._txt_col_function.setMaximumHeight(150)
        
        # Set default values
        self._set_default_values()
        
        add_col_btn = qg.QPushButton('Add Column')
        delete_column_btn = qg.QPushButton('Delete Column')
        save_table_btn = qg.QPushButton('Save New Column(s)')
        
        # Add widgets to column layout
        add_col_layout.addWidget(new_col_lb)
        add_col_layout.addWidget(self._txt_new_col_name)
        add_col_layout.addWidget(col_name1_lb)
        add_col_layout.addWidget(self._txt_col_name1)
        add_col_layout.addWidget(col_name2_lb)
        add_col_layout.addWidget(self._txt_col_name2)
        add_col_layout.addWidget(col_funct_name_lb)
        add_col_layout.addWidget(self._txt_col_funct_name)
        add_col_layout.addWidget(col_function_lb)
        add_col_layout.addWidget(self._txt_col_function)
        add_col_layout.addWidget(add_col_btn)
        add_col_layout.addWidget(delete_column_btn)
        add_col_layout.addWidget(save_table_btn)
        
        # Button_layout
        btns_widget = qg.QWidget()
        btns_layout = qg.QHBoxLayout()
        btns_widget.setLayout(btns_layout)
        btns_layout.setSpacing(4)
        btns_layout.setAlignment(qc.Qt.AlignTop)
        btns_layout.addWidget(qg.QPushButton('Test'))
        
        main_left_layout.addWidget(add_col_widget)
        main_left_layout.addWidget(btns_widget)

        # ---------------- Right Side UI --------------------------
        
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
        
        # Fill table
        self._fill_columns(table_w, table, columns)
        
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
    
        # --------------------- Connections -----------------------------
        add_col_btn.clicked.connect(self.add_column)
        self._txt_col_function.selectionChanged.connect(self._clean_txt_field)
        self._txt_col_funct_name.editingFinished.connect(self._add_function_txt)
        
    # ------------------ Class UI Methods ------------------------------
    def add_column(self):
        """
            TODO
        """
        new_col_name = self._txt_new_col_name.text()
        col_name1 = self._txt_col_name1.text()
        col_name2 = self._txt_col_name2.text()
        function_name = self._txt_col_funct_name.text()
        function = self._txt_col_function.toPlainText()
        funtion_added = self._titanic.add_new_fucntion(function_name, function)
        if not funtion_added:
            self._clean_txt = 0
            qg.QMessageBox.information(self, 'Titanic Data Analysis',
                                       'The function already exist',
                                       buttons=qg.QMessageBox.Ok,
                                       defaultButton=qg.QMessageBox.NoButton)
            return
        print ':)'
        self._set_default_values()
        
    def _set_default_values(self):
        """
            TODO
        """
        self._txt_new_col_name.clear()
        self._txt_new_col_name.setPlaceholderText('Type New Column name')
        self._txt_col_name1.clear()
        self._txt_col_name1.setPlaceholderText('Type Column name')
        self._txt_col_name2.clear()
        self._txt_col_name2.setPlaceholderText('Type Column name')
        self._txt_col_funct_name.clear()
        self._txt_col_funct_name.setPlaceholderText('Type Function Name')
        self._txt_col_function.setText('Type the function that relates'
                                       ' the columns, e.g...'
                                       '\ndef male_female_child(passenger):\n'
                                       '    age,sex = passenger\n'
                                       '    if age < 16:\n'
                                       '        return "child"\n'
                                       '    else:\n'
                                       '        return sex')
        self._clean_txt = 0

    def _clean_txt_field(self):
        """
            TODO
        """
        if self._clean_txt == 0:
            self._clean_txt = 1
            self._txt_col_function.clear()
            
    def _add_function_txt(self):
        """
            TODO
        """
        if self._clean_txt == 0:
            self._clean_txt = 1
            function_name = self._txt_col_funct_name.text()
            txt = "def %s():\n    " % function_name
            self._txt_col_function.setText(txt)
            
    def _fill_columns(self, table_w, table, columns):
        # Clear table
        table_w.clear()
        
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
            
if __name__ == '__main__':
    # Main Class instance
    titanic = main_titanic.MainTitanic()
    
    # UI
    app = qg.QApplication(sys.argv)
    main_ui = MainWindow()
    dialog = MainDialog(titanic)
    main_ui.setCentralWidget(dialog)
    main_ui.show()
    sys.exit(app.exec_())