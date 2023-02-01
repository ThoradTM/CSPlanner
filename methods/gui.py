import sys

from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSize, QThreadPool
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
from methods.runnable import WebDriver
from queue import Queue

# I hate myself
app = QApplication(sys.argv)
# Vars declared here because I fucking hate self.my
threadpool = QThreadPool()
label = QLabel()
username = QLineEdit()
password = QLineEdit()
otp = QLineEdit()
otpButton = QPushButton("Enter OTP")
layout = QVBoxLayout()
button = QPushButton("Sign in")
queue = Queue()
msg = QMessageBox()


def storeString(string):
    with open('calendar.txt', 'w') as file:
        file.write(string)


def done():
    msg.setInformativeText("Successfully connected to MyMav and gathered information")
    msg.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(960, 540))
        self.setWindowTitle("CSPlanner")

        username.setPlaceholderText("Username")
        password.setPlaceholderText("Password")
        password.setEchoMode(QLineEdit.EchoMode.Password)
        otp.setPlaceholderText("OTP")
        otpButton.clicked.connect(self.onOtpClick)

        layout.addWidget(username)
        layout.addWidget(password)
        layout.addWidget(otp)
        layout.addWidget(otpButton)
        otpButton.hide()
        otp.hide()

        button.setCheckable(True)
        button.clicked.connect(self.onClicked)

        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def onClicked(self):
        self.hide()
        username.hide()
        password.hide()
        button.hide()
        web = WebDriver(username.text(), password.text(), queue)
        web.signals.result.connect(storeString)
        web.signals.otp.connect(self.prompt)
        web.signals.finished.connect(done)
        threadpool.start(web)

    def onOtpClick(self):
        queue.put(otp.text())
        self.hide()
        otp.hide()
        otpButton.hide()

    def prompt(self):
        otp.show()
        otpButton.show()
        self.show()

