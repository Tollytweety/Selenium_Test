import time

from selenium import webdriver
from selenium.webdriver.common.by import By

wait = 5
url = "https://www.saucedemo.com/"
username = "standard_user"
password ="secret_sauce"


driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(wait)

driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "login-button").click()
time.sleep(wait)