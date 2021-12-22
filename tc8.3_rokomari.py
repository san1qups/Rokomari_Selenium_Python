import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement
import pyperclip
import openpyxl as excel


driver = webdriver.Chrome("C:\\wedriver\\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.rokomari.com/book")

driver.get("https://www.rokomari.com/login")


mail = "01888018837"
password = "lolme1011"


search_xpath = '//*[@id="j_username"]'
search_box = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.XPATH, search_xpath))
)
time.sleep(1)

pyperclip.copy(mail)

search_box.send_keys(Keys.CONTROL + "v")

time.sleep(2)

search_ypath = '//*[@id="j_password"]'
search_box = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.XPATH, search_ypath))
)
time.sleep(1)

pyperclip.copy(password)

search_box.send_keys(Keys.CONTROL + "v")

input_xpath = '//*[@id="loginForm"]/button'
input_box = driver.find_element_by_xpath(input_xpath)

input_box.send_keys(Keys.ENTER)

time.sleep(2)

stationary_xpath = '/html/body/header/div/nav/div/div[1]/ul/li[3]/a'
driver.find_element_by_xpath(stationary_xpath).click()