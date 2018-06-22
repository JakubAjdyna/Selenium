def UpdateAddress():
    #going to account page
    driver.find_element_by_class_name('account').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[3]/a').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/div/div/ul/li[9]/a[1]').click()
    element = driver.find_element_by_name("company")
    element.clear()
    element.send_keys("Test")
    driver.find_element_by_name('submitAddress').click()