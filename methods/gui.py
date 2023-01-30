from PyQt6.QtWidgets import QApplication, QWidget
import sys

# Only one QApplication instance is needed for this program
# sys.argv passes commandline arguments to it
app = QApplication(sys.argv)


window = QWidget()
window.show()


app.exec()