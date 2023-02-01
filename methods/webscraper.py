import sys
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

LOGIN = "https://mymav.utshare.utsystem.edu/psp/ARCSPRD/EMPLOYEE/SA/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL"

HOMEPAGE = "https://mymav.utshare.utsystem.edu/psc/ARCSPRD/EMPLOYEE/SA/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL"

CALENDAR = "https://mymav.utshare.utsystem.edu/psc/ARCSPRD_8/EMPLOYEE/PSFT_ACS/c/UTA_FLUID_TILES.UTA_CLASS_SCHED_FL.GBL?Page=UTA_CLASS_SCHED_FL&Action=U"
def implicit_wait_byid(driver, element):
    try:
        item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, element))
        )
        return item
    except NoSuchElementException:
        sys.exit("Error loading page content. Please try again.")


def implicit_wait_byname(driver, element):
    try:
        item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, element))
        )
        return item
    except NoSuchElementException:
        sys.exit("Error loading page content. Please try again.")


def implicit_wait_byxpath(driver, element):
    try:
        item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, element))
        )
        return item
    except NoSuchElementException:
        sys.exit("Error loading page content. Please try again.")


def fetch_data(username, password):
    chrome_options = Options()
    # point this towards your chrome browser executable
    # chrome_options.binary_location = "C:\seleniumbin\winbin\chrome-win\chrome.exe"
    # point this to the web driver that matches the version of your chrome executable
    # driver = webdriver.Chrome("C:\seleniumbin\winbin\chromedriver_win32\chromedriver.exe", options=chrome_options)

    # SOME VERSIONS OF CHROME WILL NOT WORK

    # Makes the browser run headless. For final only.
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(LOGIN)

    implicit_wait_byname(driver, "loginfmt").send_keys(username)
    time.sleep(1)
    implicit_wait_byid(driver, "idSIButton9").click()

    implicit_wait_byname(driver, "passwd").send_keys(password)
    time.sleep(1)
    implicit_wait_byid(driver, "idSIButton9").click()

    # while driver.current_url != homepage:
    implicit_wait_byid(driver, "signInAnotherWay").click()
    # driver.find_element(By.XPATH("//div[@data-value='PhoneAppNotification']"))
    # driver.find_element(By.XPATH("//div[@data-value='PhoneAppOTP']"))
    implicit_wait_byxpath(driver, "//div[@data-value='OneWaySMS']").click()
    # driver.find_element(By.XPATH("//div[@data-value='TwoWayVoiceMobile']"))
    return driver
