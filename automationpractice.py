import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
#driver.maximize_window()
wait = WebDriverWait(driver,10)

def Login():
    #going to login page
    driver.find_element_by_class_name("login").click()
    #entering email
    elem = driver.find_element_by_id("email")
    elem.send_keys("aydyn@wp.pl")
    #entering password
    elem = driver.find_element_by_id("passwd")
    elem.send_keys("Password1#")
    #loging in
    driver.find_element_by_name("SubmitLogin").click()

def Logout():
    #loging out
    driver.find_element_by_class_name("logout").click()
    time.sleep(5)

def OrderHistory():
    #going to account page
    driver.find_element_by_class_name('account').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[1]/a').click()
    
def OrderDetails():
    driver.find_element_by_xpath('//*[@id="order-list"]/tbody/tr[1]/td[7]/a[1]').click()

def OrderInvoice():
    driver.find_element_by_xpath('//*[@id="order-list"]/tbody/tr[1]/td[6]/a').click()

def OrderMessage():
    wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="sendOrderMessage"]/p[2]/select/option[2]'))
    driver.find_element_by_xpath('//*[@id="sendOrderMessage"]/p[2]/select/option[2]').click()
    elem = driver.find_element_by_name('msgText')
    elem.send_keys("Test")
    driver.find_element_by_xpath('//*[@id="sendOrderMessage"]/div/button').click()

def CreditSlip():
    driver.find_element_by_class_name('account').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[2]/a').click()

def UpdateAddress():
    #going to account page
    driver.find_element_by_class_name('account').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[3]/a').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/div/div/ul/li[9]/a[1]').click()
    elem = driver.find_element_by_name("company")
    elem.clear()
    elem.send_keys("Test")
    driver.find_element_by_name('submitAddress').click()

def AddAndDeleteAddress():
    #going to account page
    driver.find_element_by_class_name('account').click()
    #going to addressess page
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[3]/a').click()
    #going to new address page
    driver.find_element_by_xpath('//*[@id="center_column"]/div[2]/a').click()
    elem = driver.find_element_by_id('address1')
    elem.send_keys('Testing St. 1/99')
    elem = driver.find_element_by_id('city')
    elem.send_keys('Testigo')
    #selecting state from dropdown menu
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
    #deleting new address
    driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/div/div[2]/ul/li[9]/a[2]/span').click()
    #confirming delete on alert popup
    alert = driver.switch_to_alert()
    alert.accept()

def UpdatePersonalInfo():
    driver.find_element_by_class_name('account').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[4]/a').click()
    #selecting gender
    driver.find_element_by_id('id_gender2').click()
    #changing name
    elem = driver.find_element_by_id('firstname')
    elem.clear()
    elem.send_keys('Pani')
    elem = driver.find_element_by_id('lastname')
    elem.clear()
    elem.send_keys('Testeer')    
    #changing date of birth
    driver.find_element_by_xpath('//*[@id="days"]/option[32]').click()
    driver.find_element_by_xpath('//*[@id="months"]/option[13]').click()
    driver.find_element_by_xpath('//*[@id="years"]/option[40]').click()
    #changing password
    elem = driver.find_element_by_name('old_passwd')
    elem.send_keys('Password1#')
    elem = driver.find_element_by_name('passwd')
    elem.send_keys('Password#1')
    elem = driver.find_element_by_name('confirmation')
    elem.send_keys('Password#1')
    #signing up for mail subscription
    driver.find_element_by_name('newsletter').click()
    driver.find_element_by_name('optin').click()
    #saving
    driver.find_element_by_xpath('//*[@id="center_column"]/div/form/fieldset/div[11]/button').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/a').click() 
    #going back to personal informations   
    driver.find_element_by_class_name('account').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[4]/a').click()
    #selecting gender 2nd time
    driver.find_element_by_id('id_gender1').click()
    #reverting name change
    elem = driver.find_element_by_id('firstname')
    elem.clear()
    elem.send_keys('Pan')
    elem = driver.find_element_by_id('lastname')
    elem.clear()
    elem.send_keys('Tester')  
    #reverting date of birth change
    driver.find_element_by_xpath('//*[@id="days"]/option[2]').click()
    driver.find_element_by_xpath('//*[@id="months"]/option[2]').click()
    driver.find_element_by_xpath('//*[@id="years"]/option[30]').click()
    #reverting password change
    elem = driver.find_element_by_name('old_passwd')
    elem.send_keys('Password#1')
    elem = driver.find_element_by_name('passwd')
    elem.send_keys('Password1#')
    elem = driver.find_element_by_name('confirmation')
    elem.send_keys('Password1#')
    #mail subscription sign out
    driver.find_element_by_name('newsletter').click()
    driver.find_element_by_name('optin').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div/form/fieldset/div[11]/button').click()

def Wishlist():
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[2]/ul/li/a').click()
    #add a new wishlist
    element = driver.find_element_by_xpath('//*[@id="name"]')
    element.send_keys('Test wishlist')
    driver.find_element_by_name('submitWishlist').click()
    #add a new item to wishlist
    driver.find_element_by_xpath('//*[@id="best-sellers_block_right"]/div/ul/li[1]/a/img').click()
    wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="wishlist_button"]'))
    driver.find_element_by_xpath('//*[@id="wishlist_button"]').click()
    wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="product"]/div[2]/div/div/a'))
    driver.find_element_by_xpath('//*[@id="product"]/div[2]/div/div/a').click()
    #back to wishlist
    wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a'))
    driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[2]/ul/li/a').click()
    #view details    details = //*[@id="wishlist_4246"]/td[1]/a   delete = //*[@id="wishlist_4246"]/td[6]/a/i
    driver.find_element_by_link_text('Test wishlist').click()
    #change quantity
    wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="quantity_7_34"]'))
    elem = driver.find_element_by_xpath('//*[@id="quantity_7_34"]')
    elem.send_keys('1')
    #change priority
    driver.find_element_by_xpath('//*[@id="priority_7_34"]/option[1]').click()
    #save changes to a product
    driver.find_element_by_xpath('//*[@id="wlp_7_34"]/div/div[2]/div/div[2]/a/span').click()
    #send a wishlist
    driver.find_element_by_xpath('//*[@id="showSendWishlist"]').click()
    driver.find_element_by_xpath('//*[@id="showSendWishlist"]').click()
    wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="email1"]'))
    element = driver.find_element_by_xpath('//*[@id="email1"]')
    element.send_keys('test@test.pl')
    driver.find_element_by_xpath('//*[@id="block-order-detail"]/div/form/fieldset/div[11]/button').click()
    #delete wishlist
    wait.until(lambda driver: driver.find_element_by_class_name('icon-remove')
    content = driver.find_element_by_class_name("icon-remove")
    content.click()
    alert = driver.switch_to_alert()
    alert.accept


    

url = "http://automationpractice.com/index.php"
driver.get(url)
Login()
#OrderHistory()
#OrderDetails()
#OrderMessage()
#OrderInvoice()
#CreditSlip()
#UpdateAddress()
#AddAndDeleteAddress()
#UpdatePersonalInfo()
Wishlist()
Logout()
driver.close()