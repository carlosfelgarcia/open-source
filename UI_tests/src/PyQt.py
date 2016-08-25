'''
Created on Aug 4, 2016

@author: User
'''

import sys
import random
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle("Test PyQt")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        quit_action = QtGui.QAction("&Quit", self)
        quit_action.setShortcut("Ctrl+Q")
        quit_action.setStatusTip("Quit the app")
        quit_action.triggered.connect(self.close_window)
        
        text_action = QtGui.QAction("&Text Editor", self)
        text_action.setShortcut("Ctrl+E")
        text_action.setStatusTip("Open Editor")
        text_action.triggered.connect(self.editor)
        
        open_action = QtGui.QAction("&Open File", self)
        open_action.setShortcut("Ctrl+O")
        open_action.setStatusTip("Open File")
        open_action.triggered.connect(self.open_file)

        self.statusBar()
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("&File")
        file_menu.addAction(quit_action)
        file_menu.addAction(open_action)
        
        file_menu = main_menu.addMenu("&Editor")
        file_menu.addAction(text_action)

        self.home()

    def home(self):
        # Button
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_window)
        btn.resize(btn.sizeHint())
        btn.move(200, 50)
        
        # Toolbar
        quit_action = QtGui.QAction(QtGui.QIcon('python.png'), "Quit", self)
        quit_action.triggered.connect(self.close_window)
        self.toolbar = self.addToolBar("Quit")
        self.toolbar.addAction(quit_action)
        
        font_action = QtGui.QAction("Font Style", self)
        font_action.triggered.connect(self.font_style)
        self.toolbar.addAction(font_action)
        
        color_action = QtGui.QAction("Color bg", self)
        color_action.triggered.connect(self.color_bg)
        self.toolbar.addAction(color_action)
        
        # Checkbox
        check_box = QtGui.QCheckBox('Enlarge Window', self)
        check_box.move(50, 50)
        check_box.stateChanged.connect(self.enlarge_window)
        
        # Progress Bar
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(250, 100, 250, 20)
        
        # Button progress bar
        self.btn_download = QtGui.QPushButton("Download", self)
        self.btn_download.resize(self.btn_download.sizeHint())
        self.btn_download.move(250, 130)
        self.btn_download.clicked.connect(self.download)
        
        # Label Style
        self.style_label = QtGui.QLabel("Windows vista", self)
        
        # Combo Box Style
        combo_box = QtGui.QComboBox(self)
        combo_box.addItems(["motif", "Windows", "cde", "Plastique",
                            "Cleanlooks", "windowsvista"])
        combo_box.move(200, 200)
        self.style_label.move(200, 150)
        combo_box.activated[str].connect(self.style_choice)
        
        self.show()
        
    def download(self):
        counter = 0
        while counter < 100:
            counter += 0.0001
            self.progress.setValue(counter)

    def style_choice(self, text):
        self.style_label.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(100, 100, 500, 700)
        else:
            self.setGeometry(100, 100, 500, 300)

    def close_window(self):
        choice = QtGui.QMessageBox.question(self, "Quit!",
                                            "Are you sure you want to quit? ",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print "See ya!!"
            sys.exit()
    
    def font_style(self):
        font, valid = QtGui.QFontDialog().getFont()
        if valid:
            self.style_label.setFont(font)
        
    def color_bg(self):
        color = QtGui.QColorDialog.getColor()
        self.style_label.setStyleSheet("QWidget {background-color: %s}" % color.name())
        
    def editor(self):
        self.text_editor = QtGui.QTextEdit()
        self.setCentralWidget(self.text_editor)
        
    def open_file(self):
        file_path = QtGui.QFileDialog.getOpenFileName()
        with open(file_path, 'r') as file:
            self.editor()
            self.text_editor.setText(file.read())
            

def run():
    app = QtGui.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())

run()
