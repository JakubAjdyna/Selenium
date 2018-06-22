driver = webdriver.Chrome()

def Logout():
    #loging out
    driver.find_element_by_class_name("logout").click()
    time.sleep(3)