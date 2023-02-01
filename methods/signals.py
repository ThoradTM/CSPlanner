from PyQt6.QtCore import QObject, pyqtSignal


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    otp = pyqtSignal()
