# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 618)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(210, 400))
        self.frame.setMaximumSize(QtCore.QSize(210, 400))
        self.frame.setMouseTracking(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 200, 100))
        self.tabWidget.setMinimumSize(QtCore.QSize(200, 100))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit_y1 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_y1.setGeometry(QtCore.QRect(130, 10, 50, 20))
        self.lineEdit_y1.setObjectName("lineEdit_y1")
        self.lineEdit_x2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_x2.setGeometry(QtCore.QRect(30, 50, 50, 20))
        self.lineEdit_x2.setObjectName("lineEdit_x2")
        self.lineEdit_y2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_y2.setGeometry(QtCore.QRect(130, 50, 50, 20))
        self.lineEdit_y2.setObjectName("lineEdit_y2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 14, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(110, 14, 30, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 54, 30, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(110, 54, 30, 13))
        self.label_4.setObjectName("label_4")
        self.lineEdit_x1 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_x1.setGeometry(QtCore.QRect(30, 10, 50, 20))
        self.lineEdit_x1.setObjectName("lineEdit_x1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 14, 50, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 54, 50, 13))
        self.label_6.setObjectName("label_6")
        self.lineEdit_r = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_r.setGeometry(QtCore.QRect(60, 10, 60, 20))
        self.lineEdit_r.setObjectName("lineEdit_r")
        self.lineEdit_a = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_a.setGeometry(QtCore.QRect(60, 50, 60, 20))
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_clr_line = QtWidgets.QPushButton(self.frame)
        self.pushButton_clr_line.setGeometry(QtCore.QRect(110, 120, 40, 30))
        self.pushButton_clr_line.setText("")
        self.pushButton_clr_line.setCheckable(False)
        self.pushButton_clr_line.setAutoDefault(False)
        self.pushButton_clr_line.setDefault(False)
        self.pushButton_clr_line.setFlat(False)
        self.pushButton_clr_line.setObjectName("pushButton_clr_line")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(10, 130, 63, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton_clr_back = QtWidgets.QPushButton(self.frame)
        self.pushButton_clr_back.setGeometry(QtCore.QRect(110, 160, 40, 30))
        self.pushButton_clr_back.setText("")
        self.pushButton_clr_back.setObjectName("pushButton_clr_back")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(10, 170, 59, 16))
        self.label_9.setObjectName("label_9")
        self.checkBox_clr_back = QtWidgets.QCheckBox(self.frame)
        self.checkBox_clr_back.setGeometry(QtCore.QRect(10, 200, 141, 17))
        self.checkBox_clr_back.setTristate(False)
        self.checkBox_clr_back.setObjectName("checkBox_clr_back")
        self.comboBox_alg = QtWidgets.QComboBox(self.frame)
        self.comboBox_alg.setGeometry(QtCore.QRect(5, 230, 195, 22))
        self.comboBox_alg.setObjectName("comboBox_alg")
        self.comboBox_alg.addItem("")
        self.comboBox_alg.addItem("")
        self.comboBox_alg.addItem("")
        self.comboBox_alg.addItem("")
        self.comboBox_alg.addItem("")
        self.comboBox_alg.addItem("")
        self.pushButton_draw = QtWidgets.QPushButton(self.frame)
        self.pushButton_draw.setGeometry(QtCore.QRect(5, 260, 95, 23))
        self.pushButton_draw.setObjectName("pushButton_draw")
        self.pushButton_clear = QtWidgets.QPushButton(self.frame)
        self.pushButton_clear.setGeometry(QtCore.QRect(105, 260, 95, 23))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(0, 300, 205, 100))
        self.groupBox.setMinimumSize(QtCore.QSize(205, 100))
        self.groupBox.setMaximumSize(QtCore.QSize(205, 100))
        self.groupBox.setObjectName("groupBox")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_len = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_len.setGeometry(QtCore.QRect(105, 30, 95, 20))
        self.lineEdit_len.setObjectName("lineEdit_len")
        self.pushButton_time = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_time.setGeometry(QtCore.QRect(5, 60, 95, 23))
        self.pushButton_time.setObjectName("pushButton_time")
        self.pushButton_step = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_step.setGeometry(QtCore.QRect(105, 60, 95, 23))
        self.pushButton_step.setObjectName("pushButton_step")
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_5.setBuddy(self.lineEdit_r)
        self.label_6.setBuddy(self.lineEdit_a)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox_alg.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KG-3"))
        #self.lineEdit_y1.setText(_translate("MainWindow", "0"))
        #self.lineEdit_x2.setText(_translate("MainWindow", "0"))
        #self.lineEdit_y2.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "X1:"))
        self.label_2.setText(_translate("MainWindow", "Y1:"))
        self.label_3.setText(_translate("MainWindow", "X2:"))
        self.label_4.setText(_translate("MainWindow", "Y2:"))
        #self.lineEdit_x1.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Линия"))
        self.label_5.setText(_translate("MainWindow", "Радиус:"))
        self.label_6.setText(_translate("MainWindow", "Угол:"))
        self.lineEdit_r.setText(_translate("MainWindow", "200"))
        self.lineEdit_a.setText(_translate("MainWindow", "15"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Спектр"))
        self.label_8.setText(_translate("MainWindow", "Цвет линии:"))
        self.label_9.setText(_translate("MainWindow", "Цвет фона:"))
        self.checkBox_clr_back.setText(_translate("MainWindow", "Рисовать цветом фона"))
        self.comboBox_alg.setItemText(0, _translate("MainWindow", "ЦДА"))
        self.comboBox_alg.setItemText(1, _translate("MainWindow", "Брезенхема (int)"))
        self.comboBox_alg.setItemText(2, _translate("MainWindow", "Брезенхема (float)"))
        self.comboBox_alg.setItemText(3, _translate("MainWindow", "Брезенхема без ступенчатости"))
        self.comboBox_alg.setItemText(4, _translate("MainWindow", "Алгоритм Ву"))
        self.comboBox_alg.setItemText(5, _translate("MainWindow", "Библиотечный метод"))
        self.pushButton_draw.setText(_translate("MainWindow", "Нарисовать"))
        self.pushButton_clear.setText(_translate("MainWindow", "Очистить"))
        self.groupBox.setTitle(_translate("MainWindow", "Эффективность"))
        self.label_10.setText(_translate("MainWindow", "Длина отрезка:"))
        self.lineEdit_len.setText(_translate("MainWindow", "1000"))
        self.pushButton_time.setText(_translate("MainWindow", "Время"))
        self.pushButton_step.setText(_translate("MainWindow", "Ступенчатость"))

