from gui import GUI
from client import Client
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import sys


class MainController(GUI):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.main_stacked.setCurrentIndex(0)
        self.client = Client()
        self.login_button.clicked.connect(lambda: self.login_attempt())
        self.link_sign_up.clicked.connect(lambda: self.main_stacked.setCurrentIndex(1))
        self.back_button.clicked.connect(lambda: self.main_stacked.setCurrentIndex(0))
        self.sign_up_button.clicked.connect(lambda: self.sign_up())
        self.logout_button.clicked.connect(lambda: self.logout_redirect())
        self.upload_files_button.clicked.connect(lambda: self.upload_files_redirect())
        self.browse_files_button.clicked.connect(lambda: self.browse_files())
        self.upload_button.clicked.connect(lambda: self.upload_files())
        self.back_button_5.clicked.connect(lambda: self.main_stacked.setCurrentIndex(2))
        self.verified_username = None

    def login_attempt(self):
        username = self.username_sign_in.text()
        password = self.password_sign_in.text()
        if self.client.login(username, password):
            self.verified_username = username
            self.verified_username = self.verified_username[0].upper() + self.verified_username[1:]
            self.username_sign_in.clear()
            self.password_sign_in.clear()
            self.show_control_panel()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Cant find you account, {username}, with the password you provided. Try again!")
            msg.setWindowTitle("Error")
            msg.exec_()

    def sign_up(self):
        username = self.sign_up_user.text()
        password = self.sign_up_password.text()
        email = self.sign_up_email.text()
        if self.client.sign_up(username, password, email):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Sign up successful, you can login now!")
            msg.setWindowTitle("Success")
            msg.exec_()
            self.main_stacked.setCurrentIndex(0)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Username length must be more than 4 and email must be valid!")
            msg.setWindowTitle("Error")
            msg.exec_()

        self.sign_up_user.clear()
        self.sign_up_password.clear()
        self.sign_up_email.clear()


    def show_control_panel(self):
        self.main_username_label.setText(f"{self.verified_username}'s - Control Panel")
        self.main_stacked.setCurrentIndex(2)

    def logout_redirect(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Bye {self.verified_username}, it was good to see you!")
        msg.setWindowTitle("Success")
        msg.exec_()
        self.verified_username = None
        self.main_stacked.setCurrentIndex(0)

    def upload_files_redirect(self):
        self.upload_files_username_label.setText(f"{self.verified_username} - Upload Files")
        self.main_stacked.setCurrentIndex(6)


    def browse_files(self):
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self.MainWindow, "QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            self.file_path_line_edit.setText("||".join(files))

    def upload_files(self):
        for file in self.file_path_line_edit.text().split("||"):
            if file:
                self.client.upload_file(file, self.verified_username)



def main():
    app = QtWidgets.QApplication(sys.argv)
    mainwin = QtWidgets.QMainWindow()
    MainController(mainwin)
    mainwin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
