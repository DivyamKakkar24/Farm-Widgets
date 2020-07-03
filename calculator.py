# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from math import e, log10, sqrt, sin, cos, tan

from math import radians as rad

import sqlite3

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(639, 308)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        Calculator.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Farm-Widgets/Farm-Widgets/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Calculator.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Calculator)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.t1 = QtWidgets.QLineEdit(Calculator)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.t1.setFont(font)
        self.t1.setText("")
        self.t1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.t1.setObjectName("t1")
        self.horizontalLayout_2.addWidget(self.t1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.b31 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.b31.setFont(font)
        self.b31.setObjectName("b31")
        self.horizontalLayout.addWidget(self.b31)
        #'
        self.b32 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.b32.setFont(font)
        self.b32.setObjectName("b32")
        self.horizontalLayout.addWidget(self.b32)
        #'
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(18)
        self.gridLayout.setObjectName("gridLayout")
        self.b19 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b19.setFont(font)
        self.b19.setObjectName("b19")
        self.gridLayout.addWidget(self.b19, 3, 2, 1, 1)
        self.b13 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b13.setFont(font)
        self.b13.setObjectName("b13")
        self.gridLayout.addWidget(self.b13, 2, 3, 1, 1)
        self.b17 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b17.setFont(font)
        self.b17.setObjectName("b17")
        self.gridLayout.addWidget(self.b17, 1, 2, 1, 1)
        self.b4 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b4.setFont(font)
        self.b4.setObjectName("b4")
        self.gridLayout.addWidget(self.b4, 3, 5, 1, 1)
        self.b23 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b23.setFont(font)
        self.b23.setObjectName("b23")
        self.gridLayout.addWidget(self.b23, 2, 1, 1, 1)
        self.b30 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b30.setFont(font)
        self.b30.setObjectName("b30")
        self.gridLayout.addWidget(self.b30, 4, 0, 1, 1)
        self.b8 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b8.setFont(font)
        self.b8.setObjectName("b8")
        self.gridLayout.addWidget(self.b8, 2, 4, 1, 1)
        self.b14 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b14.setFont(font)
        self.b14.setObjectName("b14")
        self.gridLayout.addWidget(self.b14, 3, 3, 1, 1)
        self.b6 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b6.setFont(font)
        self.b6.setObjectName("b6")
        self.gridLayout.addWidget(self.b6, 0, 4, 1, 1)
        self.b21 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b21.setFont(font)
        self.b21.setObjectName("b21")
        self.gridLayout.addWidget(self.b21, 0, 1, 1, 1)
        self.b11 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b11.setFont(font)
        self.b11.setObjectName("b11")
        self.gridLayout.addWidget(self.b11, 0, 3, 1, 1)
        self.b27 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b27.setFont(font)
        self.b27.setObjectName("b27")
        self.gridLayout.addWidget(self.b27, 1, 0, 1, 1)
        self.b3 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.gridLayout.addWidget(self.b3, 2, 5, 1, 1)
        self.b18 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b18.setFont(font)
        self.b18.setObjectName("b18")
        self.gridLayout.addWidget(self.b18, 2, 2, 1, 1)
        self.b7 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b7.setFont(font)
        self.b7.setObjectName("b7")
        self.gridLayout.addWidget(self.b7, 1, 4, 1, 1)
        self.b5 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b5.setFont(font)
        self.b5.setObjectName("b5")
        self.gridLayout.addWidget(self.b5, 4, 5, 1, 1)
        self.b22 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b22.setFont(font)
        self.b22.setObjectName("b22")
        self.gridLayout.addWidget(self.b22, 1, 1, 1, 1)
        self.b2 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.gridLayout.addWidget(self.b2, 1, 5, 1, 1)
        self.b24 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b24.setFont(font)
        self.b24.setObjectName("b24")
        self.gridLayout.addWidget(self.b24, 3, 1, 1, 1)
        self.b16 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b16.setFont(font)
        self.b16.setObjectName("b16")
        self.gridLayout.addWidget(self.b16, 0, 2, 1, 1)
        self.b29 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b29.setFont(font)
        self.b29.setObjectName("b29")
        self.gridLayout.addWidget(self.b29, 3, 0, 1, 1)
        self.b20 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b20.setFont(font)
        self.b20.setObjectName("b20")
        self.gridLayout.addWidget(self.b20, 4, 2, 1, 1)
        self.b1 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.gridLayout.addWidget(self.b1, 0, 5, 1, 1)
        self.b15 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b15.setFont(font)
        self.b15.setObjectName("b15")
        self.gridLayout.addWidget(self.b15, 4, 3, 1, 1)
        self.b12 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b12.setFont(font)
        self.b12.setObjectName("b12")
        self.gridLayout.addWidget(self.b12, 1, 3, 1, 1)
        self.b26 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b26.setFont(font)
        self.b26.setObjectName("b26")
        self.gridLayout.addWidget(self.b26, 0, 0, 1, 1)
        self.b28 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b28.setFont(font)
        self.b28.setObjectName("b28")
        self.gridLayout.addWidget(self.b28, 2, 0, 1, 1)
        self.b10 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b10.setFont(font)
        self.b10.setObjectName("b10")
        self.gridLayout.addWidget(self.b10, 4, 4, 1, 1)
        self.b25 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b25.setFont(font)
        self.b25.setObjectName("b25")
        self.gridLayout.addWidget(self.b25, 4, 1, 1, 1)
        self.b9 = QtWidgets.QPushButton(Calculator)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b9.setFont(font)
        self.b9.setObjectName("b9")
        self.gridLayout.addWidget(self.b9, 3, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.b16.clicked.connect(self.clear)
        self.b19.clicked.connect(self.one)
        self.b14.clicked.connect(self.two)
        self.b9.clicked.connect(self.three)
        self.b8.clicked.connect(self.six)
        self.b13.clicked.connect(self.five)
        self.b18.clicked.connect(self.four)
        self.b17.clicked.connect(self.seven)
        self.b12.clicked.connect(self.eight)
        self.b7.clicked.connect(self.nine)
        self.b15.clicked.connect(self.zero)
        self.b20.clicked.connect(self.period)
        self.b1.clicked.connect(self.divide)
        self.b2.clicked.connect(self.multiply)
        self.b3.clicked.connect(self.subtract)
        self.b4.clicked.connect(self.add)
        self.b26.clicked.connect(self.leftbracket)
        self.b21.clicked.connect(self.rightbracket)
        self.b6.clicked.connect(self.modulus)
        self.b10.clicked.connect(self.pi)
        self.b11.clicked.connect(self.sqroot)
        self.b27.clicked.connect(self.square)
        self.b28.clicked.connect(self.eulers)
        self.b29.clicked.connect(self.log)
        self.b30.clicked.connect(self.reciprocal)
        self.b25.clicked.connect(self.absolute)
        self.b22.clicked.connect(self.sine)
        self.b23.clicked.connect(self.cosine)
        self.b24.clicked.connect(self.tangent)
        self.b5.clicked.connect(self.evaluate)
        self.b32.clicked.connect(self.save)
        self.b31.clicked.connect(self.history)


        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def clear(self):
        self.t1.clear()
        #print('cleared')

    def one(self):
        k = self.t1.text()
        put = str(k + '1')
        self.t1.setText(put)
        #print(k)

    def two(self):
        k = self.t1.text()
        put = str(k + '2')
        self.t1.setText(put)
        #print(k)

    def three(self):
        k = self.t1.text()
        put = str(k + '3')
        self.t1.setText(put)
        #print(k)

    def four(self):
        k = self.t1.text()
        put = str(k + '4')
        self.t1.setText(put)
        #print(k)

    def five(self):
        k = self.t1.text()
        put = str(k + '5')
        self.t1.setText(put)
        #print(k)

    def six(self):
        k = self.t1.text()
        put = str(k + '6')
        self.t1.setText(put)
        #print(k)

    def seven(self):
        k = self.t1.text()
        put = str(k + '7')
        self.t1.setText(put)
        #print(k)

    def eight(self):
        k = self.t1.text()
        put = str(k + '8')
        self.t1.setText(put)
        #print(k)

    def nine(self):
        k = self.t1.text()
        put = str(k + '9')
        self.t1.setText(put)
        #print(k)

    def zero(self):
        k = self.t1.text()
        put = str(k + '0')
        self.t1.setText(put)
        #print(k)

    def period(self):
        k = self.t1.text()
        if k == '':
            put = str(k + '0.')
            self.t1.setText(put)
        elif k[-1] == '+' or k[-1] == '-' or k[-1] == '*' or k[-1] == '/' or k[-1] == '%':
            put = str(k + '0.')
            self.t1.setText(put)
        elif '*' in k or '+' in k or '-' in k or '/' in k or '(':
            c = k.count('*') + k.count('-') + k.count('+') + k.count('/') + k.count('/')
            i = 0
            while c > 0:
                if k[i] == '*' or k[i] == '-' or k[i] == '+' or k[i] == '/' or k[i] == '(':
                    c -= 1
                i += 1
            j = k[i:]
            if '.' in j:
                put = str(k + '')
                self.t1.setText(put)
            else:
                put = str(k + '.')
                self.t1.setText(put)
        #print(k)

    def divide(self):
        k = self.t1.text()
        if k == '':
            put = str(k + '')
            self.t1.setText(put)
        elif k[-1] != '+' and k[-1] != '-' and k[-1] != '*' and k[-1] != '/' and k[-1] != '%':
            put = str(k + '/')
            self.t1.setText(put)
        else:
            k = k[:-1]
            put = str(k + '/')
            self.t1.setText(put)
        #print(k)

    def multiply(self):
        k = self.t1.text()
        if k == '':
            put = str(k + '')
            self.t1.setText(put)
        elif k[-1] != '+' and k[-1] != '-' and k[-1] != '*' and k[-1] != '/' and k[-1] != '%':
            put = str(k + '*')
            self.t1.setText(put)
        else:
            k = k[:-1]
            put = str(k + '*')
            self.t1.setText(put)
        #print(k)

    def subtract(self):
        k = self.t1.text()
        if k == '':
            put = str(k + '')
            self.t1.setText(put)
        elif k[-1] != '+' and k[-1] != '-' and k[-1] != '*' and k[-1] != '/' and k[-1] != '%':
            put = str(k + '-')
            self.t1.setText(put)
        else:
            k = k[:-1]
            put = str(k + '-')
            self.t1.setText(put)
        #print(k)

    def add(self):
        k = self.t1.text()
        if k == '':
            put = str(k + '')
            self.t1.setText(put)
        elif k[-1] != '+' and k[-1] != '-' and k[-1] != '*' and k[-1] != '/' and k[-1] != '%':
            put = str(k + '+')
            self.t1.setText(put)
        else:
            k = k[:-1]
            put = str(k + '+')
            self.t1.setText(put)
        #print(k)

    def leftbracket(self):
        k = self.t1.text()
        if k == '':
            put = str(k + '(')
            self.t1.setText(put)
        elif k[-1] == '+' or k[-1] == '-' or k[-1] == '*' or k[-1] == '/' or k[-1] == '%':
            put = str(k + '(')
            self.t1.setText(put)
        elif ('*' in k
              or
              '+' in k
              or
              '-' in k
              or
              '/' in k
              or
              '(' in k
              or
              ')' in k
              or
              '0' in k
              or
              '1' in k
              or
              '2' in k
              or
              '3' in k
              or
              '4' in k
              or
              '5' in k
              or
              '6' in k
              or
              '7' in k
              or
              '8' in k
              or
              '9' in k):
            c = (k.count('*') +
                 k.count('-') +
                 k.count('+') +
                 k.count('/') +
                 k.count('(') +
                 k.count(')') +
                 k.count('0') +
                 k.count('1') +
                 k.count('2') +
                 k.count('3') +
                 k.count('4') +
                 k.count('5') +
                 k.count('6') +
                 k.count('7') +
                 k.count('8') +
                 k.count('9'))
            i = 0
            while c > 0:
                if (k[i] == '*'
                    or
                    k[i] == '-'
                    or
                    k[i] == '+'
                    or
                    k[i] == '/'
                    or
                    k[i] == '('
                    or
                    k[i] == ')'
                    or
                    k[i] == '0'
                    or
                    k[i] == '1'
                    or
                    k[i] == '2'
                    or
                    k[i] == '3'
                    or
                    k[i] == '4'
                    or
                    k[i] == '5'
                    or
                    k[i] == '6'
                    or
                    k[i] == '7'
                    or
                    k[i] == '8'
                    or
                    k[i] == '9'):
                    c -= 1
                i += 1
            j = k[i:]
            #o = len(j)
            #k = k[:-o]
            if '(' in j:
                put = str(k + '')
                self.t1.setText(put)
            else:
                put = str(k + '*(')
                self.t1.setText(put)
        #print(k)

    def rightbracket(self):
        k = self.t1.text()
        if k == '':
            put = str(k + '')
            self.t1.setText(put)
        elif (k[-1] == ')'
              or
              k[-1] == '('
              or
              k[-1] == '+'
              or
              k[-1] == '-'
              or
              k[-1] == '*'
              or
              k[-1] == '/'):
            put = str(k + '')
            self.t1.setText(put)
        elif ('*' in k
              or
              '+' in k
              or
              '-' in k
              or
              '/' in k
              or
              ')' in k
              or
              '(' in k):
            c = k.count('*') + k.count('-') + k.count('+') + k.count('/') + k.count(')') + k.count('(')
            i = 0
            while c > 0:
                if k[i] == '*' or k[i] == '-' or k[i] == '+' or k[i] == '/' or k[i] == ')' or k[i] == '(':
                    c -= 1
                i += 1
            j = k[i:]
            if ')' in j:
                put = str(k + '')
                self.t1.setText(put)
            else:
                put = str(k + ')')
                self.t1.setText(put)
        else:
            put = str(k + ')')
            self.t1.setText(put)
        #print(k)

    def modulus(self):
        k = self.t1.text()
        if k == '':
            put = str(k + '')
            self.t1.setText(put)
        elif (k[-1] != '+'
              and
              k[-1] != '-'
              and
              k[-1] != '*'
              and
              k[-1] != '/'
              and
              k[-1] != '%'):
            put = str(k + '%')
            self.t1.setText(put)
        else:
            k = k[:-1]
            put = str(k + '%')
            self.t1.setText(put)
        #print(k)

    def pi(self):
        k = self.t1.text()
        if k == '':
            put = str(k + '3.14')
            self.t1.setText(put)
        elif (k[-1] == '+'
              or
              k[-1] == '-'
              or
              k[-1] == '*'
              or
              k[-1] == '/'
              or
              k[-1] == '%'):
            put = str(k + '3.14')
            self.t1.setText(put)
        else:
            put = str(k + '*3.14')
            self.t1.setText(put)
        #print(k)

    def sqroot(self):
        k = self.t1.text()
        if k == '':
            put = str(k + 'sqrt(')
            self.t1.setText(put)
        elif (k[-1] == '+'
              or
              k[-1] == '-'
              or
              k[-1] == '*'
              or
              k[-1] == '/'
              or
              k[-1] == '%'):
            put = str(k + 'sqrt(')
            self.t1.setText(put)
        else:
            put = str(k + '*sqrt(')
            self.t1.setText(put)
        #print(k)

    def square(self):
        k = self.t1.text()
        if k == '':
            put = str(k + '')
            self.t1.setText(put)
        elif (k[-1] == '+'
              or
              k[-1] == '-'
              or
              k[-1] == '*'
              or
              k[-1] == '/'
              or
              k[-1] == '%'):
            put = str(k + '')
            self.t1.setText(put)
        elif ('*' in k
              or
              '+' in k
              or
              '-' in k
              or
              '/' in k
              or
              '(' in k
              or
              ')' in k):
            c = k.count('*') + k.count('-') + k.count('+') + k.count('/') + k.count('(') + k.count(')')
            i = 0
            while c > 0:
                if (k[i] == '*'
                    or
                    k[i] == '-'
                    or
                    k[i] == '+'
                    or
                    k[i] == '/'
                    or
                    k[i] == '('
                    or
                    k[i] == ')'):
                    c -= 1
                i += 1
            j = k[i:]
            o = len(j)
            k = k[:-o]
            put = str(k + '({}**2)'.format(j))
            self.t1.setText(put)
        else:
            put = str('({}**2)'.format(k))
            self.t1.setText(put)
        #print(k)

    def eulers(self):
        k = self.t1.text()
        if k == '':
            put = str(k + 'e')
            self.t1.setText(put)
        elif k[-1] == '+' or k[-1] == '-' or k[-1] == '*' or k[-1] == '/' or k[-1] == '%' or k[-1] == '(':
            put = str(k + 'e')
            self.t1.setText(put)
        else:
            put = str(k + '*e')
            self.t1.setText(put)
        #print(k)

    def log(self):
        k = self.t1.text()
        if k == '':
            put = str(k + 'log10(')
            self.t1.setText(put)
        elif k[-1] == '+' or k[-1] == '-' or k[-1] == '*' or k[-1] == '/' or k[-1] == '%':
            put = str(k + 'log10(')
            self.t1.setText(put)
        else:
            put = str(k + '*log10(')
            self.t1.setText(put)
        #print(k)

    def reciprocal(self):
        k = self.t1.text()
        if k == '':
            put = str(k + '1/')
            self.t1.setText(put)
        elif k[-1] == '+' or k[-1] == '-' or k[-1] == '*' or k[-1] == '/' or k[-1] == '%':
            put = str(k + '1/')
            self.t1.setText(put)
        else:
            put = str(k + '*1/')
            self.t1.setText(put)
        #print(k)

    def absolute(self):
        k = self.t1.text()
        if k == '':
            put = str(k + 'abs(')
            self.t1.setText(put)
        elif k[-1] == '+' or k[-1] == '-' or k[-1] == '*' or k[-1] == '/' or k[-1] == '%':
            put = str(k + 'abs(')
            self.t1.setText(put)
        else:
            put = str(k + '*abs(')
            self.t1.setText(put)
        #print(k)

    def sine(self):
        k = self.t1.text()
        if k == '':
            put = str(k + 'sin(rad()')
            self.t1.setText(put)
        elif k[-1] == '+' or k[-1] == '-' or k[-1] == '*' or k[-1] == '/' or k[-1] == '%':
            put = str(k + 'sin(rad()')
            self.t1.setText(put)
        else:
            put = str(k + '*sin(rad()')
            self.t1.setText(put)
        #print(k)

    def cosine(self):
        k = self.t1.text()
        if k == '':
            put = str(k + 'cos(rad()')
            self.t1.setText(put)
        elif k[-1] == '+' or k[-1] == '-' or k[-1] == '*' or k[-1] == '/' or k[-1] == '%':
            put = str(k + 'cos(rad()')
            self.t1.setText(put)
        else:
            put = str(k + '*cos(rad()')
            self.t1.setText(put)
        #print(k)

    def tangent(self):
        k = self.t1.text()
        if k == '':
            put = str(k + 'tan(rad()')
            self.t1.setText(put)
        elif k[-1] == '+' or k[-1] == '-' or k[-1] == '*' or k[-1] == '/' or k[-1] == '%':
            put = str(k + 'tan(rad()')
            self.t1.setText(put)
        else:
            put = str(k + '*tan(rad()')
            self.t1.setText(put)
        #print(k)

    def evaluate(self):
        k = self.t1.text()
        put = str(eval(k))
        self.t1.setText('')
        self.t1.setText(put)

    def save(self):
        k = self.t1.text()
        try:
            MyInput = sqlite3.connect('Calc_history.db')
            curi = MyInput.cursor()
            curi.execute("INSERT INTO Operations (Input) VALUES(?);", (k,))
            MyInput.commit()
            #print('updated')
            self.delete()
        except:
            print('error in operation')
            MyInput.rollback()
        MyInput.close()

    def delete(self):
        # deleting third-last
        MyInput = sqlite3.connect('Calc_history.db')
        curi = MyInput.cursor()
        curi.execute("SELECT * FROM count;")
        z = curi.fetchone()
        # print(z)
        curi.execute("DELETE FROM Operations WHERE rowid = '"+str(z[0])+"';")
        # print('deleted')
        # count update
        curi.execute("UPDATE count SET c = '"+str(z[0] + 1)+"';")
        # print('counted')
        MyInput.commit()
        MyInput.close()

    def history(self):
        from calc_history import Ui_history
        Dialog = QtWidgets.QDialog()
        ui = Ui_history()
        ui.setupUi(Dialog)
        Dialog.exec()

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.b31.setText(_translate("Calculator", "History"))
        self.b19.setText(_translate("Calculator", "1"))
        self.b13.setText(_translate("Calculator", "5"))
        self.b17.setText(_translate("Calculator", "7"))
        self.b4.setText(_translate("Calculator", "+"))
        self.b23.setText(_translate("Calculator", "cos"))
        self.b30.setText(_translate("Calculator", "1/x"))
        self.b8.setText(_translate("Calculator", "6"))
        self.b14.setText(_translate("Calculator", "2"))
        self.b6.setText(_translate("Calculator", "%"))
        self.b21.setText(_translate("Calculator", ")"))
        self.b11.setText(_translate("Calculator", "√"))
        self.b27.setText(_translate("Calculator", "x²"))
        self.b3.setText(_translate("Calculator", "−"))
        self.b18.setText(_translate("Calculator", "4"))
        self.b7.setText(_translate("Calculator", "9"))
        self.b5.setText(_translate("Calculator", "="))
        self.b22.setText(_translate("Calculator", "sin"))
        self.b2.setText(_translate("Calculator", "×"))
        self.b24.setText(_translate("Calculator", "tan"))
        self.b16.setText(_translate("Calculator", "C"))
        self.b29.setText(_translate("Calculator", "log"))
        self.b20.setText(_translate("Calculator", "."))
        self.b1.setText(_translate("Calculator", "÷"))
        self.b15.setText(_translate("Calculator", "0"))
        self.b12.setText(_translate("Calculator", "8"))
        self.b26.setText(_translate("Calculator", "("))
        self.b28.setText(_translate("Calculator", "e"))
        self.b10.setText(_translate("Calculator", "π"))
        self.b25.setText(_translate("Calculator", "|x|"))
        self.b9.setText(_translate("Calculator", "3"))
        self.b32.setText(_translate("Calculator", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QWidget()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
