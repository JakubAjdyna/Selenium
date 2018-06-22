def OrderHistoryAndDetails():
    #going to account page
    driver.find_element_by_class_name('account').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[1]/a').click()
    #going to order details
    driver.find_element_by_xpath('//*[@id="order-list"]/tbody/tr[1]/td[7]/a[1]').click()
    #getting invoice
    driver.find_element_by_xpath('//*[@id="order-list"]/tbody/tr[1]/td[6]/a').click()
    #sending order message
    wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="sendOrderMessage"]/p[2]/select/option[2]'))
    driver.find_element_by_xpath('//*[@id="sendOrderMessage"]/p[2]/select/option[2]').click()
    element = driver.find_element_by_name('msgText')
    element.send_keys("Test")
    driver.find_element_by_xpath('//*[@id="sendOrderMessage"]/div/button').click()