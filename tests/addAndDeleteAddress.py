def AddAndDeleteAddress():
    #going to account page
    driver.find_element_by_class_name('account').click()
    #going to addressess page
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[3]/a').click()
    #going to new address page
    driver.find_element_by_xpath('//*[@id="center_column"]/div[2]/a').click()
    #adding new address data
    element = driver.find_element_by_id('address1')
    element.send_keys('Testing St. 1/99')
    element = driver.find_element_by_id('city')
    element.send_keys('Testigo')
    driver.find_element_by_xpath('//*[@id="id_state"]/option[6]').click()
    element = driver.find_element_by_id('postcode')
    element.send_keys('00000')
    element = driver.find_element_by_id('phone')
    element.send_keys('+1555555555')
    element = driver.find_element_by_id('phone_mobile')
    element.send_keys('+1555555555')
    element = driver.find_element_by_id('other')
    element.send_keys('Test')
    element = driver.find_element_by_name('alias')
    element.clear()
    element.send_keys('Test address')
    driver.find_element_by_id('submitAddress').click()
    #deleting new address
    driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/div/div[2]/ul/li[9]/a[2]/span').click()
    #confirming delete on alert popup
    alert = driver.switch_to_alert()
    alert.accept()