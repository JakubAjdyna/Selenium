import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

def Login():
    driver.find_element_by_class_name("login").click()
    elem = driver.find_element_by_id("email")
    elem.send_keys("aydyn@wp.pl")
    elem = driver.find_element_by_id("passwd")
    elem.send_keys("Password1#")
    driver.find_element_by_name("SubmitLogin").click()

def Logout():
    driver.find_element_by_class_name("logout").click()

def OrderHistory():
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[1]/a').click()
    
def OrderDetails():
    driver.find_element_by_xpath('//*[@id="order-list"]/tbody/tr[1]/td[7]/a[1]').click()
    time.sleep(3)

def OrderInvoice():
    driver.find_element_by_xpath('//*[@id="order-list"]/tbody/tr[1]/td[6]/a').click()
    time.sleep(3)

def OrderMessage():
    driver.find_element_by_xpath('//*[@id="sendOrderMessage"]/p[2]/select/option[2]').click()
    elem = driver.find_element_by_name("msgText")
    elem.send_keys("Test")
    driver.find_element_by_xpath('//*[@id="sendOrderMessage"]/div/button').click()
    time.sleep(3)

url = "http://automationpractice.com/index.php"
driver.get(url)
Login()
OrderHistory()
OrderDetails()
OrderMessage()
OrderInvoice()
Logout()
driver.close()