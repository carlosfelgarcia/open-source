'''
Created on Sep 2, 2016

@author: co2_k
'''


import PyQt4.QtGui as qg
import PyQt4.QtCore as qc
import sys


# ----------------------------- UI ---------------------------------------
class MainWindow(qg.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 800, 600)
        


class MainDialog(qg.QDialog):
    def __init__(self):
        qg.QDialog.__init__(self)
        qg.QDialog.__init__(self)
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setObjectName('InterpolateIt')
        self.setWindowTitle('Interpolate It')
        self.setFixedWidth(340)
        
        self.setLayout(qg.QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        
        scroll_area = qg.QScrollArea()
        scroll_area.setFocusPolicy(qc.Qt.NoFocus)
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(qc.Qt.ScrollBarAlwaysOff)
        self.layout().addWidget(scroll_area)

        main_widget = qg.QWidget()
        main_layout = qg.QVBoxLayout()
        main_widget.setLayout(main_layout)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setAlignment(qc.Qt.AlignTop)
        scroll_area.setWidget(main_widget)
        
        self.inter_layout = qg.QVBoxLayout()
        self.inter_layout.setContentsMargins(0, 0, 0, 0)
        self.inter_layout.setSpacing(0)
        self.inter_layout.setAlignment(qc.Qt.AlignTop)
        main_layout.addLayout(self.inter_layout)
        
        button_layout = qg.QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setAlignment(qc.Qt.AlignRight)
        new_btn = qg.QPushButton('New...')
        button_layout.addWidget(new_btn)
        main_layout.addLayout(button_layout)
        
        inter_widget = InterpolateItWidget()
        inter_widget.hide_close()
        self.inter_layout.addWidget(inter_widget)
        
        self.list_widgets = []
        self.list_widgets.append(inter_widget)
        
        new_btn.clicked.connect(self.add_new)

    def add_new(self):
        new_inter_widget = InterpolateItWidget()
        self.list_widgets.append(new_inter_widget)
        self.inter_layout.addWidget(new_inter_widget)
        self.connect(new_inter_widget, qc.SIGNAL('CLOSE'), self.remove)
        new_inter_widget.setFixedHeight(0)
        new_inter_widget._animation_expand(True)
        
    def remove(self, new_widget):
        self.list_widgets.remove(new_widget)
        self.connect(new_widget, qc.SIGNAL('DELETE'), self.delete)
        new_widget._animation_expand(False)
        
    def delete(self, new_widget):
        self.inter_layout.removeWidget(new_widget)
        new_widget._animation = None
        new_widget.deleteLater()
        

# ------------------------------- UI ---------------------------------------
class InterpolateItWidget(qg.QFrame):
    def __init__(self):
        qg.QFrame.__init__(self)
        self.setFixedHeight(150)
        
        self.setLayout(qg.QVBoxLayout())
        self.layout().setAlignment(qc.Qt.AlignTop)
        self.layout().setContentsMargins(5, 5, 5, 5)
        self.layout().setSpacing(5)
        
        title_layout = qg.QHBoxLayout()
        title_txt = qg.QLineEdit('Untitled')
        self.exit_btn = qg.QPushButton('X')
        self.exit_btn.setFixedWidth(40)
        title_layout.addWidget(title_txt)
        title_layout.addWidget(self.exit_btn)
        self.layout().addLayout(title_layout)
        
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
        self.slider_start_lb = qg.QLabel('Start')
        self.slider = qg.QSlider(qc.Qt.Horizontal)
        self.slider_end_lb = qg.QLabel('End')
        slider_layout.addWidget(self.slider_start_lb)
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(self.slider_end_lb)
        self.layout().addLayout(slider_layout)
        
        check_layout = qg.QHBoxLayout()
        self.trans_chk = qg.QCheckBox('Transform')
        self.attrs_chk = qg.QCheckBox('UD Attributes')
        self.attrs_chk.setCheckState(qc.Qt.Checked)
        check_layout.addWidget(self.trans_chk)
        check_layout.addSpacerItem(qg.QSpacerItem(5, 5, qg.QSizePolicy.Expanding))
        check_layout.addWidget(self.attrs_chk)
        self.layout().addLayout(check_layout)
        
        self.exit_btn.clicked.connect(self.remove)
        
        self.store_btn.clicked.connect(self.enable_btns)
        
        self.set_btns(False)
        
    def set_btns(self, value):
        self.reset_btn.setEnabled(value)
        self.end_btn.setEnabled(value)
        self.clean_btn.setEnabled(value)
        self.start_btn.setEnabled(value)
        self.slider_start_lb.setEnabled(value)
        self.slider.setEnabled(value)
        self.slider_end_lb.setEnabled(value)
        self.trans_chk.setEnabled(value)
        self.attrs_chk.setEnabled(value)
        
    def enable_btns(self):
        self.set_btns(True)
        
    def hide_close(self):
        self.exit_btn.setVisible(False)
        
    def remove(self):
        self.emit(qc.SIGNAL('CLOSE'), self)
    
    def delete_widget(self):
        self.emit(qc.SIGNAL('DELETE'), self)
        
    # ----------------------------- Animation ----------------------------------

    def _animation_expand(self, value):
        size_animation = qc.QPropertyAnimation(self, 'geometry')
        
        geometry = self.geometry()
        width = geometry.width()
        x, y, _, _ = geometry.getCoords()
        
        size_start = qc.QRect(x, y, width, int(not(value)) * 150)
        size_end = qc.QRect(x, y, width, int(value) * 150)
        
        size_animation.setStartValue(size_start)
        size_animation.setEndValue(size_end)
        size_animation.setDuration(300)
        
        anim_curve = qc.QEasingCurve()
        if value:
            anim_curve.setType(qc.QEasingCurve.InQuad)
        else:
            anim_curve.setType(qc.QEasingCurve.OutQuad)
            
        size_animation.setEasingCurve(anim_curve)
        
        size_animation.valueChanged.connect(self._force_resize)
        if not value:
            size_animation.finished.connect(self.delete_widget)
        
        self._animation = size_animation
        size_animation.start(qc.QAbstractAnimation.DeleteWhenStopped)
        
    def _force_resize(self, new_height):
        self.setFixedHeight(new_height.toRect().height())


def run():
    app = qg.QApplication(sys.argv)
    
    main_win = MainWindow()
    main_dialog = MainDialog()
    main_dialog.setParent(main_win)
    size = main_dialog.size()
    
    dock_widget = qg.QDockWidget()
    dock_widget.setFixedHeight(size.height())
    dock_widget.setFixedWidth(size.width())
    dock_widget.setWidget(main_dialog)
    dock_widget.setAllowedAreas(qc.Qt.AllDockWidgetAreas)
    main_win.addDockWidget(qc.Qt.RightDockWidgetArea, dock_widget)
    
    main_win.show()
    sys.exit(app.exec_())

run()