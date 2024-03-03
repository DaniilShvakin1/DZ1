from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(437, 354)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 61, 31))
        self.label.setStyleSheet("font: 75 italic 12pt \"Amiri\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 71, 31))
        self.label_2.setStyleSheet("font: 75 italic 12pt \"Amiri\";")
        self.label_2.setObjectName("label_2")
        self.login = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.login.setGeometry(QtCore.QRect(120, 70, 141, 31))
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password.setGeometry(QtCore.QRect(120, 140, 141, 31))
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setObjectName("password")
        self.rememberMe = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.rememberMe.setGeometry(QtCore.QRect(80, 210, 131, 31))
        self.rememberMe.setObjectName("rememberMe")
        self.login_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(140, 270, 101, 41))
        self.login_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 127);\n"
"border-radius: 15px;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.login_btn.setObjectName("login_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Логин"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.login.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.password.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.rememberMe.setText(_translate("MainWindow", "Запомнить меня"))
        self.login_btn.setText(_translate("MainWindow", "Войти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())