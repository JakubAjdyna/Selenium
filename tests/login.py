driver = webdriver.Chrome()

def Login():
    #going to login page
    driver.find_element_by_class_name("login").click()
    #entering email
    element = driver.find_element_by_id("email")
    element.send_keys("aydyn@wp.pl")
    #entering password
    element = driver.find_element_by_id("passwd")
    element.send_keys("Password1#")
    #loging in
    driver.find_element_by_name("SubmitLogin").click()