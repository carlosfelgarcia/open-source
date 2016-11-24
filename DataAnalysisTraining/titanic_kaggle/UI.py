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
import main_titanic
from bokeh.layouts import column

# Constants
TABLE_SIZE = 700
INFO = ['Mean', 'Value Count']

class MainWindow(qg.QMainWindow):
    '''
    MainWindow
    '''

    def __init__(self):
        '''
        Constructor
        '''
        # Variables
        self._actions = []
        self._menus = []
        
        # Main Window
        qg.QMainWindow.__init__(self)
        self.setWindowTitle('Data Analysis Tool')
        pos = qg.QApplication.desktop().cursor().pos()
        screen = qg.QApplication.desktop().screenNumber(pos)
        centerPoint = qg.QApplication.desktop().screenGeometry(screen).center()
        self.setGeometry(centerPoint.x() / 2, centerPoint.y() / 2, 1020, 720)
        
        # Add menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        
        # Add file actions & sub-menus
        self._create_actions()
        file_menu.addActions(self._actions)
        self._add_sub_menus(file_menu)

    def _add_sub_menus(self, file_menu):
        
        # ------------------- Load Data SubMenu Start -------------------------
        # Add Menu
        load_menu = qg.QMenu('&Load Data', self)
        file_menu.insertMenu(self._actions[-1], load_menu)
        
        # Add Actions
        action_file = qg.QAction("&Load Data From File", self)
        action_file.setStatusTip("Load data from file")
        
        action_spider = qg.QAction("&Send Spider", self)
        action_spider.setStatusTip("Send Spider and load data")
        
        load_menu.addAction(action_file)
        load_menu.addAction(action_spider)
        
        # Connections
        action_file.triggered.connect(self._load_file)
        action_spider.triggered.connect(self._send_spider)
        # ------------------- Load Data SubMenu End -------------------------
    
    def _create_actions(self):
        '''
        Added the file actions to a pre-existing list
        '''
        # Menu actions
        quit_action = qg.QAction("&Quit", self)
        quit_action.setShortcut("Ctrl+Q")
        quit_action.setStatusTip("Quit the app")
        
        save_action = qg.QAction("&Save DataFrame", self)
        save_action.setShortcut("Ctrl+s")
        save_action.setStatusTip("Save DataFrame to csv file")
        
        # Connections
        quit_action.triggered.connect(self._close_window)
        save_action.triggered.connect(self._save_df)
        
        # Add Actions to the list
        self._actions.append(save_action)
        self._actions.append(quit_action)
        
    def _close_window(self):
        """
        TODO
        """
        main_dialog = self.centralWidget()
        msn = 'Are you sure you want to quit?'
        ans = main_dialog.default_question(msn)
        if ans:
            sys.exit()
        
    def _load_file(self):
        """
        TODO
        """
        main_dialog = self.centralWidget()
        tittle = 'Choose the file you want to load'
        file_path = str(qg.QFileDialog.getOpenFileName(self, tittle))
        data = main_dialog.titanic.get_data_file(file_path)
        main_dialog.set_table(data)
        main_dialog.fill_columns()
        
    def _send_spider(self):
        """
        TODO
        """
        print 'Coming soon'
        
    def _save_df(self):
        """
        TODO
        """
        tittle = 'Choose the path where you want to save the file'
        op = qg.QFileDialog.ReadOnly
        file_path = qg.QFileDialog.getSaveFileName(self,
                                                   tittle,
                                                   filter='*.csv',
                                                   options=op)
        # Get the QDialog
        main_dialog = self.centralWidget()
        main_dialog.titanic.save_df(str(file_path))


class MainDialog(qg.QDialog):
    '''
    This is the main dialog
    '''
    def __init__(self, titanic):
        qg.QDialog.__init__(self)
        
        # World instance
        self.titanic = titanic
        
        self.setLayout(qg.QHBoxLayout())
        self.layout().setContentsMargins(5, 5, 5, 5)
        self.layout().setSpacing(2)
        
        main_widget = qg.QWidget()
        #main_widget.setStyleSheet('QWidget {background-color : rgb(227, 227, 227);}')
        
        # Widget for tab1
        page1_widget = qg.QWidget()
        
        # Main Layout
        main_layout = qg.QHBoxLayout()
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(50)
        
        # ---------------- Left Side UI --------------------------
        main_left_layout = qg.QVBoxLayout()
        main_left_layout.setContentsMargins(5, 5, 5, 5)
        main_left_layout.setSpacing(10)
        
        # ---------------------- Add column ----------------------
        col_widget = qg.QWidget()
        col_widget.setFixedHeight(400)
        col_widget.setFixedWidth(450)
        add_col_layout = qg.QVBoxLayout()
        col_widget.setLayout(add_col_layout)
        col_widget.layout().setAlignment(qc.Qt.AlignTop)
        col_widget.layout().setSpacing(10)

        # Font
        font = qg.QFont()
        font.setBold(True)
        font.setCapitalization(qg.QFont.Capitalize)
        font.setPixelSize(12)
        
        new_col_lb = qg.QLabel('Add new Column')
        new_col_lb.setFont(font)
        new_col_lb.setAlignment(qc.Qt.AlignHCenter)
        new_col_name_lb = qg.QLabel('New column name')
        new_col_name_lb.setFont(font)
        self._txt_new_col_name = qg.QLineEdit()
        self._txt_new_col_name.setMinimumWidth(400)
        
        cols_names_lb = qg.QLabel('Columns')
        cols_names_lb.setFont(font)
        self._txt_cols_names = qg.QLineEdit()
        
        col_funct_name_lb = qg.QLabel('Fuction name')
        col_funct_name_lb.setFont(font)
        self._clean_txt = 0
        self._txt_col_funct_name = qg.QLineEdit()
        reg_ex = qc.QRegExp("[a-z0-9_]+")
        text_validator = qg.QRegExpValidator(reg_ex, self._txt_col_funct_name)
        self._txt_col_funct_name.setValidator(text_validator)
        col_function_lb = qg.QLabel('Function')
        col_function_lb.setFont(font)
        self._txt_col_function = qg.QTextEdit()
        self._txt_col_function.setMaximumHeight(150)
        
        # Set default values
        self._set_default_values()
        
        add_col_btn = qg.QPushButton('Add Column')
        delete_column_btn = qg.QPushButton('Delete Column(s)')
        
        # Add widgets to column layout
        add_col_layout.addWidget(new_col_lb)
        add_col_layout.addWidget(new_col_name_lb)
        add_col_layout.addWidget(self._txt_new_col_name)
        add_col_layout.addWidget(cols_names_lb)
        add_col_layout.addWidget(self._txt_cols_names)
        add_col_layout.addWidget(col_funct_name_lb)
        add_col_layout.addWidget(self._txt_col_funct_name)
        add_col_layout.addWidget(col_function_lb)
        add_col_layout.addWidget(self._txt_col_function)
        add_col_layout.addWidget(add_col_btn)
        add_col_layout.addWidget(delete_column_btn)
        
        # -------------------- Plot Layout ----------------------------
        plot_widget = qg.QWidget()
        plot_layout = qg.QVBoxLayout()
        plot_widget.setLayout(plot_layout)
        plot_layout.setSpacing(4)
        plot_layout.setAlignment(qc.Qt.AlignTop)
        
        data_analysis_lb = qg.QLabel('Data Analysis')
        data_analysis_lb.setFont(font)
        data_analysis_lb.setAlignment(qc.Qt.AlignHCenter)
        plot_type_lb = qg.QLabel('Plot type')
        plot_type_lb.setFont(font)
        
        self._plot_menu = qg.QComboBox()
        self._plot_menu.addItems(self.titanic.get_plot_functions())
        
        self._column_names_lb = qg.QLabel('Attributes: Column')
        self._column_names_lb.setFont(font)
        self._txt_col_names = qg.QLineEdit()
        
        plot_btn = qg.QPushButton('Show Plot')
        
        # Add widgets to plot layout
        plot_layout.addWidget(data_analysis_lb)
        plot_layout.addWidget(plot_type_lb)
        plot_layout.addWidget(self._plot_menu)
        plot_layout.addWidget(self._column_names_lb)
        plot_layout.addWidget(self._txt_col_names)
        plot_layout.addWidget(plot_btn)
        
        # -------------------- Additional info -----------------------
        info_widget = qg.QWidget()
        info_layout = qg.QVBoxLayout()
        info_widget.setLayout(info_layout)
        info_layout.setSpacing(4)
        info_layout.setAlignment(qc.Qt.AlignTop)
        
        add_info_lb = qg.QLabel('Additional Information')
        add_info_lb.setFont(font)
        add_info_lb.setAlignment(qc.Qt.AlignHCenter)
        
        font_disclaimer = qg.QFont()
        font_disclaimer.setPixelSize(12)
        
        disclaimer_lb = qg.QLabel('Select the column you want to get the '
                                  'information from')
        disclaimer_lb.setFont(font_disclaimer)
        
        info_type_lb = qg.QLabel('Request Info')
        info_type_lb.setFont(font)
        
        self._info_menu = qg.QComboBox()
        self._info_menu.addItems(INFO)
        
        info_btn = qg.QPushButton('Get Information')
        
        info_layout.addWidget(add_info_lb)
        info_layout.addWidget(disclaimer_lb)
        info_layout.addWidget(info_type_lb)
        info_layout.addWidget(self._info_menu)
        info_layout.addWidget(info_btn)
        
        # Add main widgets
        main_left_layout.addWidget(col_widget)
        main_left_layout.addWidget(plot_widget)
        main_left_layout.addWidget(info_widget)

        # ---------------- Right Side UI --------------------------
        
        # Tab Widget
        self._tab_widget = qg.QTabWidget()
        self._tab_widget.setTabPosition(0)
        
        # Table Layout
        table_layout = qg.QHBoxLayout()
        table_layout.setContentsMargins(5, 5, 5, 5)
        table_layout.setAlignment(qc.Qt.AlignTop)
        
        # Table widget
        self._table_w1 = qg.QTableWidget()
        self._table_w1.setMinimumWidth(TABLE_SIZE)
        self._table_w1.setMinimumHeight(TABLE_SIZE)
        
        self._tab_widget.addTab(self._table_w1, 'Table 1')
        table_layout.addWidget(self._tab_widget)
        
        # Added Main Layout
        main_layout.addLayout(main_left_layout)
        main_layout.addLayout(table_layout)
        main_widget.setLayout(main_layout)
        
        self.layout().addWidget(main_widget)
    
        # --------------------- Connections -----------------------------
        add_col_btn.clicked.connect(self.add_column)
        delete_column_btn.clicked.connect(self.del_column)
        self._txt_col_function.selectionChanged.connect(self._clean_txt_field)
        self._txt_col_funct_name.editingFinished.connect(self._add_function_txt)
        plot_btn.clicked.connect(self.show_plot)
        # Used the other way to connect as I can get the text as parameter
        self.connect(self._plot_menu,
                     qc.SIGNAL('currentIndexChanged(QString)'),
                     self._change_label)

    # ------------------ Class UI Methods ------------------------------
    def _change_label(self, func_name):
        """
            TODO
        """
        label = self.titanic.get_plot_label(str(func_name))
        self._column_names_lb.setText('Attributes: {0}'.format(label))
    
    def del_column(self):
        """
            TODO
        """
        # Get all the values
        col_selected = self._table_w1.selectedItems()
        column_names = []
        last_name = ''
        for column_item in col_selected:
            column_index = self._table_w1.column(column_item)
            item = self._table_w1.horizontalHeaderItem(column_index)
            column_name = str(item.text())
            if column_name == last_name:
                continue
            last_name = column_name
            column_names.append(column_name)

        # Get new data frame
        self._table = self.titanic.del_column(column_names)
          
        # reload table values
        self.fill_columns()
        
    def add_column(self):
        """
            TODO
        """
        # Get all the values
        new_col_name = str(self._txt_new_col_name.text())
        cols_names = str(self._txt_cols_names.text())
        function_name = str(self._txt_col_funct_name.text())
        function = str(self._txt_col_function.toPlainText())
        
        # Check if all the values are filled
        if not self._check_fields([new_col_name, cols_names,
                                   function_name, function]):
            return
        
        # Check the columns existence
        current_columns = self._table.keys()
        if cols_names not in current_columns:
            self.default_warning('One of the columns does not exist, please '
                                 'check the names and try again')
            return

        # Add new function
        function_added = self.titanic.add_new_fucntion(function_name, function)
        if function_added == -1:
            msn = 'Error: There are some Syntax errors in your function'
            self.default_warning(msn)
            return
        elif function_added == 0:
            msn = 'This function already exist, do you want to continue?'
            ans = self.default_question(msn)
            # 0 = no 1= yes
            if not ans:
                self._clean_txt = 0
                self.default_warning('The function was not added,'
                                     ' please try again')
                return
        
        # Add the column and get the updated data frame
        self._table = self.titanic.add_new_column(new_col_name, cols_names,
                                                  function_name)
        
        # reload table values
        self.fill_columns()
        
        # Set the UI back to default
        self._set_default_values()
        
    def _check_fields(self, fields):
        """
            TODO
        """
        for value in fields:
            if value == '' or value is None:
                self._clean_txt = 0
                self.default_warning('All the values need to be filled')
                return False
        return True
    
    def default_warning(self, msn):
        """
        TODO
        """
        qg.QMessageBox.warning(self, 'Titanic Data Analysis',
                               msn,
                               buttons=qg.QMessageBox.Ok,
                               defaultButton=qg.QMessageBox.NoButton)
        
    def default_question(self, msn, btn1='No', btn2='Yes'):
        """
        TODO
        """
        return qg.QMessageBox.question(self, 'Titanic Data Analysis',
                                       msn,
                                       btn1,
                                       btn2,
                                       defaultButtonNumber=0)
    
    def _set_default_values(self):
        """
            TODO
        """
        self._txt_new_col_name.clear()
        self._txt_new_col_name.setPlaceholderText('Type New Column name')
        self._txt_cols_names.clear()
        self._txt_cols_names.setPlaceholderText('Type Columns names')
        self._txt_col_funct_name.clear()
        self._txt_col_funct_name.setPlaceholderText('Type Function Name')
        self._txt_col_function.setText('Type the function that relates'
                                       ' the columns, e.g...'
                                       '\ndef funct_name(*Args):\n'
                                       '    function...')
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
            
    def fill_columns(self, columns=None):
        """
            TODO
        """
        # Clear table
        self._table_w1.setRowCount(0)
        self._table_w1.setColumnCount(0)
        
        # Get columns
        if not columns:
            columns = sorted(self._table.keys())
            
        # Add values to the table
        for column in columns:
            col_num = self._table_w1.columnCount()
            row_total_num = self._table_w1.rowCount()
            self._table_w1.insertColumn(col_num)
            col_item = qg.QTableWidgetItem(column)
            self._table_w1.setHorizontalHeaderItem(col_num, col_item)
            if isinstance(self._table[column], collections.Iterable):
                for i in xrange(len(self._table[column])):
                    value = ''
                    if isinstance(value, np.float64):
                        value = np.int(self._table[column][i])

                    elif isinstance(value, str):
                        value = str(self._table[column][i])
                        if value == 'nan':
                            value = '---'
                    
                    table_item = qg.QTableWidgetItem(value)
                    
                    if i >= row_total_num:
                        self._table_w1.insertRow(i)
                    self._table_w1.setItem(i, col_num, table_item)
            else:
                self._table_w1.insertRow(row_total_num)
                table_item = qg.QTableWidgetItem(self._table[column])
                self._table_w1.setItem(row_total_num, col_num, table_item)
                
        self._table_w1.resizeColumnsToContents()
        self._table_w1.resizeRowsToContents()
        
    def show_plot(self):
        """
        TODO
        """
        vals = str(self._txt_col_names.text())
        if not vals:
            self.default_warning('Please fill the values you want to analyze')
            return
        values = [val.strip() for val in vals.split(',')]
        if any(map(lambda v: v not in self._table.keys(), values)):
            self.default_warning("Some values don't match column name")
            return
        graph = str(self._plot_menu.currentText())
        plot_graph = self.titanic.get_plot(values, graph)
        if not plot_graph:
            self.default_warning("The values don't match the graph you want")
            return
        plot_graph.fig.show()
        
    def set_table(self, data):
        """
        TODO
        """
        self._table = data
    
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