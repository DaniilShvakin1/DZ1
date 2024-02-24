import sys

from PyQt6.QtWidgets import QApplicftion, QApplication

import login_window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #init login window
login_window_ = login_window.login_window

login_window_.show()

sys.exit(app.exec())




