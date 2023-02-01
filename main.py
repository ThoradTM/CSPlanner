import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from methods.gui import MainWindow

# Only one QApplication instance is needed for this program
# sys.argv passes commandline arguments to it
app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()



# username = input("What is your username?")
# password = input("What is your password?")
#
# text = fetch_data(username, password)
#
# print(text)
