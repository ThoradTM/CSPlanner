from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget

from methods.webscraper import fetch_data


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(960, 540))
        self.setWindowTitle("CSPlanner")

        self.label = QLabel()

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        layout = QVBoxLayout()
        layout.addWidget(self.username)
        layout.addWidget(self.password)

        button = QPushButton("Sign in")
        button.setCheckable(True)
        button.clicked.connect(self.onClicked)

        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def onClicked(self):
        text_info = fetch_data(self.username.text(), self.password.text())
        print(text_info)
