# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.v1_widget = PlotWidget(self.centralwidget)
        self.v1_widget.setObjectName("v1_widget")
        self.verticalLayout.addWidget(self.v1_widget)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(60, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.v1_speed_bar = QtWidgets.QSlider(self.centralwidget)
        self.v1_speed_bar.setOrientation(QtCore.Qt.Horizontal)
        self.v1_speed_bar.setObjectName("v1_speed_bar")
        self.gridLayout.addWidget(self.v1_speed_bar, 3, 1, 1, 3)
        self.v1_btn_add_signal = QtWidgets.QPushButton(self.centralwidget)
        self.v1_btn_add_signal.setObjectName("v1_btn_add_signal")
        self.gridLayout.addWidget(self.v1_btn_add_signal, 0, 0, 1, 1)
        self.v1_btn_clone_signal2 = QtWidgets.QPushButton(self.centralwidget)
        self.v1_btn_clone_signal2.setObjectName("v1_btn_clone_signal2")
        self.gridLayout.addWidget(self.v1_btn_clone_signal2, 2, 1, 1, 1)
        self.v1_btn_start_pause = QtWidgets.QPushButton(self.centralwidget)
        self.v1_btn_start_pause.setCheckable(True)
        self.v1_btn_start_pause.setObjectName("v1_btn_start_pause")
        self.gridLayout.addWidget(self.v1_btn_start_pause, 0, 1, 1, 1)
        self.v1_btn_signal_start_point = QtWidgets.QPushButton(self.centralwidget)
        self.v1_btn_signal_start_point.setObjectName("v1_btn_signal_start_point")
        self.gridLayout.addWidget(self.v1_btn_signal_start_point, 0, 2, 1, 1)
        self.v1_speed_label = QtWidgets.QLabel(self.centralwidget)
        self.v1_speed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.v1_speed_label.setObjectName("v1_speed_label")
        self.gridLayout.addWidget(self.v1_speed_label, 3, 0, 1, 1)
        self.v1_btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.v1_btn_save.setObjectName("v1_btn_save")
        self.gridLayout.addWidget(self.v1_btn_save, 2, 0, 1, 1)
        self.v1_btn_link = QtWidgets.QPushButton(self.centralwidget)
        self.v1_btn_link.setObjectName("v1_btn_link")
        self.gridLayout.addWidget(self.v1_btn_link, 1, 1, 1, 1)
        self.v1_btn_restart = QtWidgets.QPushButton(self.centralwidget)
        self.v1_btn_restart.setObjectName("v1_btn_restart")
        self.gridLayout.addWidget(self.v1_btn_restart, 1, 0, 1, 1)
        self.v1_btn_zoom_in = QtWidgets.QPushButton(self.centralwidget)
        self.v1_btn_zoom_in.setObjectName("v1_btn_zoom_in")
        self.gridLayout.addWidget(self.v1_btn_zoom_in, 2, 2, 1, 1)
        self.v1_btn_move_left = QtWidgets.QPushButton(self.centralwidget)
        self.v1_btn_move_left.setObjectName("v1_btn_move_left")
        self.gridLayout.addWidget(self.v1_btn_move_left, 1, 2, 1, 1)
        self.v1_btn_zoom_out = QtWidgets.QPushButton(self.centralwidget)
        self.v1_btn_zoom_out.setObjectName("v1_btn_zoom_out")
        self.gridLayout.addWidget(self.v1_btn_zoom_out, 2, 3, 1, 1)
        self.v1_btn_signal_end_point = QtWidgets.QPushButton(self.centralwidget)
        self.v1_btn_signal_end_point.setObjectName("v1_btn_signal_end_point")
        self.gridLayout.addWidget(self.v1_btn_signal_end_point, 0, 3, 1, 1)
        self.v1_btn_move_right = QtWidgets.QPushButton(self.centralwidget)
        self.v1_btn_move_right.setObjectName("v1_btn_move_right")
        self.gridLayout.addWidget(self.v1_btn_move_right, 1, 3, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 0, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.v2_widget = PlotWidget(self.centralwidget)
        self.v2_widget.setObjectName("v2_widget")
        self.verticalLayout_2.addWidget(self.v2_widget)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(60, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.v2_btn_add_signal = QtWidgets.QPushButton(self.centralwidget)
        self.v2_btn_add_signal.setObjectName("v2_btn_add_signal")
        self.gridLayout_2.addWidget(self.v2_btn_add_signal, 0, 0, 1, 1)
        self.v2_btn_start_pause = QtWidgets.QPushButton(self.centralwidget)
        self.v2_btn_start_pause.setCheckable(True)
        self.v2_btn_start_pause.setObjectName("v2_btn_start_pause")
        self.gridLayout_2.addWidget(self.v2_btn_start_pause, 0, 1, 1, 1)
        self.v2_btn_signal_start_point = QtWidgets.QPushButton(self.centralwidget)
        self.v2_btn_signal_start_point.setObjectName("v2_btn_signal_start_point")
        self.gridLayout_2.addWidget(self.v2_btn_signal_start_point, 0, 2, 1, 1)
        self.v2_btn_signal_end_point = QtWidgets.QPushButton(self.centralwidget)
        self.v2_btn_signal_end_point.setObjectName("v2_btn_signal_end_point")
        self.gridLayout_2.addWidget(self.v2_btn_signal_end_point, 0, 3, 1, 1)
        self.v2_btn_restart = QtWidgets.QPushButton(self.centralwidget)
        self.v2_btn_restart.setObjectName("v2_btn_restart")
        self.gridLayout_2.addWidget(self.v2_btn_restart, 1, 0, 1, 1)
        self.v2_btn_link = QtWidgets.QPushButton(self.centralwidget)
        self.v2_btn_link.setObjectName("v2_btn_link")
        self.gridLayout_2.addWidget(self.v2_btn_link, 1, 1, 1, 1)
        self.v2_btn_move_left = QtWidgets.QPushButton(self.centralwidget)
        self.v2_btn_move_left.setObjectName("v2_btn_move_left")
        self.gridLayout_2.addWidget(self.v2_btn_move_left, 1, 2, 1, 1)
        self.v2_btn_move_right = QtWidgets.QPushButton(self.centralwidget)
        self.v2_btn_move_right.setObjectName("v2_btn_move_right")
        self.gridLayout_2.addWidget(self.v2_btn_move_right, 1, 3, 1, 1)
        self.v2_btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.v2_btn_save.setObjectName("v2_btn_save")
        self.gridLayout_2.addWidget(self.v2_btn_save, 2, 0, 1, 1)
        self.v2_btn_clone_signal1 = QtWidgets.QPushButton(self.centralwidget)
        self.v2_btn_clone_signal1.setObjectName("v2_btn_clone_signal1")
        self.gridLayout_2.addWidget(self.v2_btn_clone_signal1, 2, 1, 1, 1)
        self.v2_btn_zoom_in = QtWidgets.QPushButton(self.centralwidget)
        self.v2_btn_zoom_in.setObjectName("v2_btn_zoom_in")
        self.gridLayout_2.addWidget(self.v2_btn_zoom_in, 2, 2, 1, 1)
        self.v2_btn_zoom_out = QtWidgets.QPushButton(self.centralwidget)
        self.v2_btn_zoom_out.setObjectName("v2_btn_zoom_out")
        self.gridLayout_2.addWidget(self.v2_btn_zoom_out, 2, 3, 1, 1)
        self.v2_speed_label = QtWidgets.QLabel(self.centralwidget)
        self.v2_speed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.v2_speed_label.setObjectName("v2_speed_label")
        self.gridLayout_2.addWidget(self.v2_speed_label, 3, 0, 1, 1)
        self.v2_speed_bar = QtWidgets.QSlider(self.centralwidget)
        self.v2_speed_bar.setOrientation(QtCore.Qt.Horizontal)
        self.v2_speed_bar.setObjectName("v2_speed_bar")
        self.gridLayout_2.addWidget(self.v2_speed_bar, 3, 1, 1, 3)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.menuFile.addAction(self.actionOpen_File)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "View_1"))
        self.v1_btn_add_signal.setText(_translate("MainWindow", "add_signal"))
        self.v1_btn_add_signal.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.v1_btn_clone_signal2.setText(_translate("MainWindow", "clone_signal_2"))
        self.v1_btn_start_pause.setText(_translate("MainWindow", "start/pause"))
        self.v1_btn_start_pause.setShortcut(_translate("MainWindow", "Space"))
        self.v1_btn_signal_start_point.setText(_translate("MainWindow", "sig_start"))
        self.v1_speed_label.setText(_translate("MainWindow", "Speed"))
        self.v1_btn_save.setText(_translate("MainWindow", "save"))
        self.v1_btn_link.setText(_translate("MainWindow", "link"))
        self.v1_btn_restart.setText(_translate("MainWindow", "restart"))
        self.v1_btn_zoom_in.setText(_translate("MainWindow", "zoom_in"))
        self.v1_btn_zoom_in.setShortcut(_translate("MainWindow", "Ctrl+Up"))
        self.v1_btn_move_left.setText(_translate("MainWindow", "move_left"))
        self.v1_btn_move_left.setShortcut(_translate("MainWindow", "Left"))
        self.v1_btn_zoom_out.setText(_translate("MainWindow", "zoom_out"))
        self.v1_btn_zoom_out.setShortcut(_translate("MainWindow", "Ctrl+Down"))
        self.v1_btn_signal_end_point.setText(_translate("MainWindow", "sig_end"))
        self.v1_btn_move_right.setText(_translate("MainWindow", "move_right"))
        self.v1_btn_move_right.setShortcut(_translate("MainWindow", "Right"))
        self.label_2.setText(_translate("MainWindow", "View_2"))
        self.v2_btn_add_signal.setText(_translate("MainWindow", "add_signal"))
        self.v2_btn_add_signal.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.v2_btn_start_pause.setText(_translate("MainWindow", "start/pause"))
        self.v2_btn_start_pause.setShortcut(_translate("MainWindow", "Shift+Space"))
        self.v2_btn_signal_start_point.setText(_translate("MainWindow", "sig_start"))
        self.v2_btn_signal_end_point.setText(_translate("MainWindow", "sig_end"))
        self.v2_btn_restart.setText(_translate("MainWindow", "restart"))
        self.v2_btn_link.setText(_translate("MainWindow", "link"))
        self.v2_btn_move_left.setText(_translate("MainWindow", "move_left"))
        self.v2_btn_move_left.setShortcut(_translate("MainWindow", "Shift+Left"))
        self.v2_btn_move_right.setText(_translate("MainWindow", "move_right"))
        self.v2_btn_move_right.setShortcut(_translate("MainWindow", "Shift+Right"))
        self.v2_btn_save.setText(_translate("MainWindow", "save"))
        self.v2_btn_clone_signal1.setText(_translate("MainWindow", "clone_signal_1"))
        self.v2_btn_zoom_in.setText(_translate("MainWindow", "zoom_in"))
        self.v2_btn_zoom_in.setShortcut(_translate("MainWindow", "Ctrl+Shift+Up"))
        self.v2_btn_zoom_out.setText(_translate("MainWindow", "zoom_out"))
        self.v2_btn_zoom_out.setShortcut(_translate("MainWindow", "Ctrl+Shift+Down"))
        self.v2_speed_label.setText(_translate("MainWindow", "Speed"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
