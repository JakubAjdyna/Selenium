import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import *
from wishlist import *
from logout import *

driver = webdriver.Chrome()
#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.maximize_window()
wait = WebDriverWait(driver,10)

url = "http://automationpractice.com/index.php"
driver.get(url)
login()
#orderHistoryAndDetails()
#creditSlip()
#updateAddress()
#addAndDeleteAddress()
#updatePersonalInfo()
wishlist()
logout()
driver.close()