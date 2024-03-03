from PyQt6.QtWidgets import QLineEdit, QCheckBox

from config import set_config
from config import read_config
from Login_window_ui import Ui_MainWindow

import loader

import loader


def get_field(ui: Ui_MainWindow) -> list[QLineEdit]:
    return [
        ui.login,
        ui.password,
    ]


def get_checkboxes(ui: Ui_MainWindow) -> list[QCheckBox]:
    return [
        ui.rememberMe
    ]



def login_btn_clicked():
    fields = get_field(loader.login_window_ui)

    login, password = fields[0], fields[1]

    remember_me = get_checkboxes(loader.login_window_ui)[0]

    if login.text() == 'Daniil' and password.text() == '12345':
        if remember_me.isChecked():
            set_config('config.txt', 'login', login.text())
            set_config('config.txt', 'password', password.text())
            print('authed with save')
        else:
            print('authed without save')
    else:
        print('not ok')


def logic(ui: Ui_MainWindow):
    login_btn = ui.login_btn

    login_btn.clicked.connect(login_btn_clicked)