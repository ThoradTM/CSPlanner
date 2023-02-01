from PyQt6.QtCore import QRunnable, pyqtSlot
from methods.signals import WorkerSignals
from methods.webscraper import *
import time


class WebDriver(QRunnable):
    def __init__(self, username, password, queue):
        QRunnable.__init__(self)
        self.queue = queue
        self.password = password
        self.username = username
        self.signals = WorkerSignals()

    def run(self):
        driver = fetch_data(self.username, self.password)
        self.signals.otp.emit()
        val = None
        while val is None:
            time.sleep(.5)
            val = self.queue.get()
        implicit_wait_byname(driver, "otc").send_keys(val)
        implicit_wait_byid(driver, "idSubmit_SAOTCC_Continue").click()
        driver.get(CALENDAR)
        calendartext = implicit_wait_byid(driver, "PT_MAIN").text
        print(calendartext)
        driver.close()
        # self.signals.result(calendartext)
        self.signals.finished()
