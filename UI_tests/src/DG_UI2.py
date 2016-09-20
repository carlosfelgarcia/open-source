'''
Created on Sep 2, 2016

@author: co2_k
'''


import PyQt4.QtGui as qg
import PyQt4.QtCore as qc

import sys

from customUI.button import DT_Button, DT_ButtonThin, DT_CloseButton
from customUI.checkbox import DT_Checkbox
from customUI.label import DT_Label
from customUI.line_edit import DT_LineEdit
from customUI.slider import DT_Slider


# ----------------------------- UI ---------------------------------------
class MainWindow(qg.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 800, 600)
        # Read Style sheet
        style_sheet_file = qc.QFile('scheme.qss')
        style_sheet_file.open(qc.QFile.ReadOnly)
        self.setStyleSheet(qc.QLatin1String(style_sheet_file.readAll()))


class MainDialog(qg.QDialog):
    def __init__(self):
        qg.QDialog.__init__(self)
        qg.QDialog.__init__(self)
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setObjectName('InterpolateIt')
        self.setWindowTitle('Interpolate It')
        self.setFixedWidth(314)
        
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
        new_btn = DT_Button('New...')
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
        self.setFrameStyle(qg.QFrame.Panel | qg.QFrame.Raised)
        
        self.setLayout(qg.QVBoxLayout())
        self.layout().setAlignment(qc.Qt.AlignTop)
        self.layout().setContentsMargins(3, 1, 3, 3)
        self.layout().setSpacing(0)
        self.setFixedHeight(150)
        
        main_widget = qg.QWidget()
        main_widget.setLayout(qg.QVBoxLayout())
        main_widget.layout().setContentsMargins(2, 2, 2, 2)
        main_widget.layout().setSpacing(5)
        main_widget.setFixedHeight(140)
        main_widget.setFixedWidth(290)
        
        graphics_scene = qg.QGraphicsScene()
        graphics_view = qg.QGraphicsView()
        graphics_view.setScene(graphics_scene)
        graphics_view.setHorizontalScrollBarPolicy(qc.Qt.ScrollBarAlwaysOff)
        graphics_view.setVerticalScrollBarPolicy(qc.Qt.ScrollBarAlwaysOff)
        graphics_view.setFocusPolicy(qc.Qt.NoFocus)
        graphics_view.setSizePolicy(qg.QSizePolicy.Minimum,
                                    qg.QSizePolicy.Minimum)
        graphics_view.setStyleSheet("QGraphicsView {border-style: none;}")
        self.layout().addWidget(graphics_view)
        self.main_widget_proxy = graphics_scene.addWidget(main_widget)
        main_widget.setParent(graphics_view)
        
        title_layout = qg.QHBoxLayout()
        title_txt = DT_LineEdit()
        title_txt.setPlaceholderMessage('Untitled')
        self.exit_btn = DT_CloseButton('X')
        self.exit_btn.setObjectName('roundedButton')
        title_layout.addWidget(title_txt)
        title_layout.addWidget(self.exit_btn)
        main_widget.layout().addLayout(title_layout)
        
        buttons_1_layout = qg.QHBoxLayout()
        self.store_btn = DT_Button('Store Items')
        self.clean_btn = DT_Button('Clear Items')
        buttons_1_layout.addSpacerItem(qg.QSpacerItem(5, 5,
                                                      qg.QSizePolicy.Expanding))
        buttons_1_layout.addWidget(self.store_btn)
        buttons_1_layout.addWidget(self.clean_btn)
        buttons_1_layout.addSpacerItem(qg.QSpacerItem(5, 5,
                                                      qg.QSizePolicy.Expanding))
        main_widget.layout().addLayout(buttons_1_layout)
        
        buttons_2_layout = qg.QHBoxLayout()
        self.start_btn = DT_ButtonThin('Store Start')
        self.reset_btn = DT_ButtonThin('Reset')
        self.end_btn = DT_ButtonThin('Store Ends')
        buttons_2_layout.addWidget(self.start_btn)
        buttons_2_layout.addWidget(self.reset_btn)
        buttons_2_layout.addWidget(self.end_btn)
        main_widget.layout().addLayout(buttons_2_layout)
        
        slider_layout = qg.QHBoxLayout()
        self.slider_start_lb = DT_Label('Start')
        self.slider = DT_Slider()
        self.slider.setRange(0, 49)
        self.slider.setOrientation(qc.Qt.Horizontal)
        self.slider_end_lb = DT_Label('End')
        slider_layout.addWidget(self.slider_start_lb)
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(self.slider_end_lb)
        main_widget.layout().addLayout(slider_layout)
        
        check_layout = qg.QHBoxLayout()
        self.trans_chk = DT_Checkbox('Transform')
        self.attrs_chk = DT_Checkbox('UD Attributes')
        self.attrs_chk.setCheckState(qc.Qt.Checked)
        check_layout.addWidget(self.trans_chk)
        check_layout.addSpacerItem(qg.QSpacerItem(5, 5,
                                                  qg.QSizePolicy.Expanding))
        check_layout.addWidget(self.attrs_chk)
        main_widget.layout().addLayout(check_layout)
        
        # Connections
        self.exit_btn.clicked.connect(self.remove)
        self.store_btn.clicked.connect(self.enable_btns)
        self.clean_btn.clicked.connect(self.clear_btns)
        self.set_btns(False)
        self.slider.valueChanged.connect(self.change_glow)
        
    def change_glow(self, value):
        glow_value = int(float(value) / self.slider.maximum() * 100)
        self.slider_start_lb.setGlowValue(100 - glow_value)
        self.slider_end_lb.setGlowValue(glow_value)
        
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
        
    def clear_btns(self):
        self.set_btns(False)
        self.slider.setValue(0)
        
    def enable_btns(self):
        self.set_btns(True)
        
    def hide_close(self):
        self.exit_btn.setVisible(False)
        
    def remove(self):
        self.emit(qc.SIGNAL('CLOSE'), self)
    
    def delete_widget(self):
        self.emit(qc.SIGNAL('DELETE'), self)
        
    # ----------------------------- Animation ---------------------------------

    def _animation_expand(self, value):
        size_animation = qc.QPropertyAnimation(self, 'geometry')
        opacity_anim = qc.QPropertyAnimation(self.main_widget_proxy, 'opacity')
        
        # Animation Opacity
        opacity_anim.setStartValue(not(value))
        opacity_anim.setEndValue(value)
        opacity_anim.setDuration(200)
        opacity_anim_curve = qc.QEasingCurve()
        if value:
            opacity_anim_curve.setType(qc.QEasingCurve.InQuad)
        else:
            opacity_anim_curve.setType(qc.QEasingCurve.OutQuad)
        opacity_anim.setEasingCurve(opacity_anim_curve)
        
        # def size of the geometry
        geometry = self.geometry()
        width = geometry.width()
        x, y, _, _ = geometry.getCoords()
        size_start = qc.QRect(x, y, width, int(not(value)) * 150)
        size_end = qc.QRect(x, y, width, int(value) * 150)
        
        # Animation for geometry
        size_animation.setStartValue(size_start)
        size_animation.setEndValue(size_end)
        size_animation.setDuration(300)
        anim_curve = qc.QEasingCurve()
        if value:
            anim_curve.setType(qc.QEasingCurve.InQuad)
        else:
            anim_curve.setType(qc.QEasingCurve.OutQuad)
        size_animation.setEasingCurve(anim_curve)
        
        # Animation sequence
        self._animation = qc.QSequentialAnimationGroup()
        
        if value:
            self.main_widget_proxy.setOpacity(0)
            self._animation.addAnimation(size_animation)
            self._animation.addAnimation(opacity_anim)
            self._animation.finished.connect(self._animation.clear)
        
        else:
            self.main_widget_proxy.setOpacity(1)
            self._animation.addAnimation(opacity_anim)
            self._animation.addAnimation(size_animation)
            self._animation.finished.connect(self._animation.clear)
            self._animation.finished.connect(self.delete_widget)
        
        size_animation.valueChanged.connect(self._force_resize)

        self._animation.start(qc.QAbstractAnimation.DeleteWhenStopped)
        
    # --------------------------------- Methods ------------------------------
    
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
