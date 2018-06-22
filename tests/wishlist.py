driver = webdriver.Chrome()

def Wishlist():
    #go to wishlists
    driver.find_element_by_class_name('account').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[2]/ul/li/a').click()
    #add a new wishlist
    element = driver.find_element_by_xpath('//*[@id="name"]')
    element.send_keys('Test wishlist')
    driver.find_element_by_name('submitWishlist').click()
    #add a new item to wishlist
    driver.find_element_by_xpath('//*[@id="best-sellers_block_right"]/div/ul/li[1]/a/img').click()
    wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="wishlist_button"]'))
    driver.find_element_by_xpath('//*[@id="wishlist_button"]').click()
    wait.until(lambda driver: driver.find_element_by_class_name('fancybox-close'))
    driver.find_element_by_class_name('fancybox-close').click()
    #back to wishlist
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[2]/ul/li/a').click()
    #view details
    driver.find_element_by_link_text('Test wishlist').click()
    #change quantity
    wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="quantity_7_34"]'))
    element = driver.find_element_by_xpath('//*[@id="quantity_7_34"]')
    element.send_keys('1')
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
    driver.find_element_by_class_name("icon-remove").click()
    wait.until(EC.alert_is_present())
    alert = driver.switch_to_alert()
    alert.accept()