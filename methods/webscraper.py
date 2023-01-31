from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time


def fetch_data(username, password):
    chrome_options = Options()
    # point this towards your chrome browser executable
    # chrome_options.binary_location = "C:\seleniumbin\winbin\chrome-win\chrome.exe"
    # point this to the web driver that matches the version of your chrome executable
    # driver = webdriver.Chrome("C:\seleniumbin\winbin\chromedriver_win32\chromedriver.exe", options=chrome_options)

    # SOME VERSIONS OF CHROME WILL NOT WORK

    # Makes the browser run headless. For final only.
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    login = "https://mymav.utshare.utsystem.edu/psp/ARCSPRD/EMPLOYEE/SA/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL"

    homepage= "https://mymav.utshare.utsystem.edu/psc/ARCSPRD/EMPLOYEE/SA/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL"

    calendar = "https://mymav.utshare.utsystem.edu/psc/ARCSPRD_8/EMPLOYEE/PSFT_ACS/c/UTA_FLUID_TILES.UTA_CLASS_SCHED_FL.GBL?Page=UTA_CLASS_SCHED_FL&Action=U"

    driver.get(login)
    delay = 1 # seconds


    time.sleep(1)
    driver.find_element(By.NAME, "loginfmt").send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(1)
    driver.find_element(By.NAME, "passwd").send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(5)
    #while driver.current_url != homepage:
    driver.find_element(By.ID, "signInAnotherWay").click()
    time.sleep(5)
        #driver.find_element(By.XPATH("//div[@data-value='PhoneAppNotification']"))
        #driver.find_element(By.XPATH("//div[@data-value='PhoneAppOTP']"))
    driver.find_element(By.XPATH, "//div[@data-value='OneWaySMS']").click()
    time.sleep(3)
        #driver.find_element(By.XPATH("//div[@data-value='TwoWayVoiceMobile']"))
    driver.find_element(By.NAME, "otc").send_keys(input("Enter your OTP: "))
    time.sleep(3)
    driver.find_element(By.ID, "idSubmit_SAOTCC_Continue").click()
    time.sleep(3)

    driver.get(calendar)
    time.sleep(1)
    calendartext = driver.find_element(By.ID, "PT_MAIN").text
    time.sleep(1)
    driver.close()

    return calendartext
