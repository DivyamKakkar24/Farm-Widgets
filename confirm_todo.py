# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirm_todo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Confirm(object):
    def setupUi(self, Confirm):
        Confirm.setObjectName("Confirm")
        Confirm.resize(280, 105)
        Confirm.setMinimumSize(QtCore.QSize(280, 105))
        Confirm.setMaximumSize(QtCore.QSize(280, 105))
        self.buttonBox = QtWidgets.QDialogButtonBox(Confirm)
        self.buttonBox.setGeometry(QtCore.QRect(40, 60, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Confirm)
        self.label.setGeometry(QtCore.QRect(40, 20, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Confirm)
        self.buttonBox.accepted.connect(Confirm.accept)
        self.buttonBox.rejected.connect(Confirm.reject)
        QtCore.QMetaObject.connectSlotsByName(Confirm)

    def retranslateUi(self, Confirm):
        _translate = QtCore.QCoreApplication.translate
        Confirm.setWindowTitle(_translate("Confirm", "Confirmation"))
        self.label.setText(_translate("Confirm", "Task will be deleted"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Confirm = QtWidgets.QDialog()
    ui = Ui_Confirm()
    ui.setupUi(Confirm)
    Confirm.show()
    sys.exit(app.exec_())
