from PyQt6.QtWidgets import QMainWindow, QLineEdit, QCheckBox, QPushButton

from PyQt6 import uic
# init window
login_window = QMainWindow()
# init elements
uic.loadUi("ui/login_window.ui", login_window)
# init fields
login_field: QLineEdit = login_window.findChild(QLineEdit, "login")

password_field: QLineEdit = login_window.findChild(QLineEdit, "password")

remember_me = login_window.findChild(QCheckBox, "rememberMe")

login_btn: QPushButton
