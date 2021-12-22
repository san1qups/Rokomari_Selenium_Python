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

driver.find_element_by_xpath('//*[@id="login-registration"]/div/section/div[2]/div[1]/p[2]').click()

fullname = "Sayed Atique Newaz"

mail = "2017-2-60-067@std.ewubd.edu"

mobile = "01888018837"

password = "lolme1011"

search_name_xpath = '//*[@id="nm"]'
search_box = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.XPATH, search_name_xpath))
)
time.sleep(1)

pyperclip.copy(fullname)

search_box.send_keys(Keys.CONTROL + "v")

time.sleep(1)

search_mail_xpath = '//*[@id="js-email"]'
search_box = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.XPATH, search_mail_xpath))
)
time.sleep(1)

pyperclip.copy(mail)

search_box.send_keys(Keys.CONTROL + "v")

time.sleep(1)

search_mobile_xpath = '//*[@id="js-phone"]'
search_box = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.XPATH, search_mobile_xpath))
)
time.sleep(1)

pyperclip.copy(mobile)

search_box.send_keys(Keys.CONTROL + "v")

time.sleep(1)

search_pass_xpath = '//*[@id="pwd"]'
search_box = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.XPATH, search_pass_xpath))
)
time.sleep(1)

pyperclip.copy(password)

search_box.send_keys(Keys.CONTROL + "v")

time.sleep(1)

search_capcha_xpath = '//*[@id="accountForm"]/div[6]/div/div'
driver.find_element_by_xpath(search_capcha_xpath).click()
time.sleep(1)
input_xpath = '//*[@id="accountForm"]/button'
input_box = driver.find_element_by_xpath(input_xpath)

input_box.send_keys(Keys.ENTER)
#