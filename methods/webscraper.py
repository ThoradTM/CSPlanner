from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def fetch_data(username, password):
    chrome_options = Options()
    # point this towards your chrome browser executable
    # chrome_options.binary_location = "C:\seleniumbin\winbin\chrome-win\chrome.exe"
    # point this to the web driver that matches the version of your chrome executable
    # driver = webdriver.Chrome("C:\seleniumbin\winbin\chromedriver_win32\chromedriver.exe", options=chrome_options)

    # SOME VERSIONS OF CHROME WILL NOT WORK
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome()

    username = input("What is your username?")
    password = input("What is your password?")

    login = "https://mymav.utshare.utsystem.edu/psp/ARCSPRD/EMPLOYEE/SA/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL"

    calendar = "https://mymav.utshare.utsystem.edu/psc/ARCSPRD_8/EMPLOYEE/PSFT_ACS/c/UTA_FLUID_TILES.UTA_CLASS_SCHED_FL.GBL?Page=UTA_CLASS_SCHED_FL&Action=U"

    driver.get(login)
    time.sleep(1)
    driver.find_element(By.NAME, "loginfmt").send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(1)
    driver.find_element(By.NAME, "passwd").send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(1)
    driver.get(calendar)
    time.sleep(1)
    calendartext = driver.find_element(By.ID, "PT_MAIN")
    time.sleep(1)
    driver.close()

    return calendartext
