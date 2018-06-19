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
    time.sleep(3)

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

def CreditSlip():
    driver.find_element_by_class_name('account').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[2]/a').click()
    time.sleep(3)

def UpdateAddress():
    driver.find_element_by_class_name('account').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[3]/a').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/div/div/ul/li[9]/a[1]').click()
    elem = driver.find_element_by_name("company")
    elem.clear()
    elem.send_keys("Test")
    driver.find_element_by_name('submitAddress').click()

def AddAddress():
    driver.find_element_by_class_name('account').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[3]/a').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div[2]/a').click()
    elem = driver.find_element_by_id('address1')
    elem.send_keys('Testing St. 1/99')
    elem = driver.find_element_by_id('city')
    elem.send_keys('Testigo')
    driver.find_element_by_xpath('//*[@id="id_state"]/option[6]').click()
    elem = driver.find_element_by_id('postcode')
    elem.send_keys('00000')
    elem = driver.find_element_by_id('phone')
    elem.send_keys('+1555555555')
    elem = driver.find_element_by_id('phone_mobile')
    elem.send_keys('+1555555555')
    elem = driver.find_element_by_id('other')
    elem.send_keys('Test')
    elem = driver.find_element_by_name('alias')
    elem.clear()
    elem.send_keys('Test address')
    driver.find_element_by_id('submitAddress').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/div/div[2]/ul/li[9]/a[2]/span').click()
    alert = driver.switch_to_alert()
    alert.accept()



url = "http://automationpractice.com/index.php"
driver.get(url)
Login()
OrderHistory()
OrderDetails()
OrderMessage()
OrderInvoice()
CreditSlip()
UpdateAddress()
AddAddress()
Logout()
driver.close()