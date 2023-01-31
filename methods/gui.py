import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(960, 540))
        self.setWindowTitle("CSPlanner")
        button = QPushButton("Hello World!")

        self.setCentralWidget(button)
