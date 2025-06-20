# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/ecc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Tiêu đề
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 20, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("ECC Cipher")

        # Nút Generate Keys
        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(600, 25, 100, 30))
        self.btn_gen_keys.setObjectName("btn_gen_keys")
        self.btn_gen_keys.setText("Gen keys")

        # Label + TextEdit: Message (txt_info)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 80, 100, 20))
        self.label_5.setObjectName("label_5")
        self.label_5.setText("Message")

        self.txt_info = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(80, 100, 300, 100))
        self.txt_info.setObjectName("txt_info")

        # Label + TextEdit: Signature (txt_sign)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 80, 100, 20))
        self.label_6.setObjectName("label_6")
        self.label_6.setText("Signature")

        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(420, 100, 300, 100))
        self.txt_sign.setObjectName("txt_sign")

        # Button Sign
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(210, 220, 100, 30))
        self.btn_sign.setObjectName("btn_sign")
        self.btn_sign.setText("Sign")

        # Button Verify
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(550, 220, 100, 30))
        self.btn_verify.setObjectName("btn_verify")
        self.btn_verify.setText("Verify")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " ECC Cipher"))
        self.label_5.setText(_translate("MainWindow", "Infor"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_gen_keys.setText(_translate("MainWindow", "Gen keys"))
        self.label_6.setText(_translate("MainWindow", "Signature"))
        self.btn_verify.setText(_translate("MainWindow", "verify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
