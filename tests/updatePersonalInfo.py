def UpdatePersonalInfo():
    driver.find_element_by_class_name('account').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[4]/a').click()
    #selecting gender
    driver.find_element_by_id('id_gender2').click()
    #changing name
    element = driver.find_element_by_id('firstname')
    element.clear()
    element.send_keys('Pani')
    element = driver.find_element_by_id('lastname')
    element.clear()
    element.send_keys('Testeer')    
    #changing date of birth
    driver.find_element_by_xpath('//*[@id="days"]/option[32]').click()
    driver.find_element_by_xpath('//*[@id="months"]/option[13]').click()
    driver.find_element_by_xpath('//*[@id="years"]/option[40]').click()
    #changing password
    element = driver.find_element_by_name('old_passwd')
    element.send_keys('Password1#')
    element = driver.find_element_by_name('passwd')
    element.send_keys('Password#1')
    element = driver.find_element_by_name('confirmation')
    element.send_keys('Password#1')
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
    element = driver.find_element_by_id('firstname')
    element.clear()
    element.send_keys('Pan')
    element = driver.find_element_by_id('lastname')
    element.clear()
    element.send_keys('Tester')  
    #reverting date of birth change
    driver.find_element_by_xpath('//*[@id="days"]/option[2]').click()
    driver.find_element_by_xpath('//*[@id="months"]/option[2]').click()
    driver.find_element_by_xpath('//*[@id="years"]/option[30]').click()
    #reverting password change
    element = driver.find_element_by_name('old_passwd')
    element.send_keys('Password#1')
    element = driver.find_element_by_name('passwd')
    element.send_keys('Password1#')
    element = driver.find_element_by_name('confirmation')
    element.send_keys('Password1#')
    #mail subscription sign out
    driver.find_element_by_name('newsletter').click()
    driver.find_element_by_name('optin').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div/form/fieldset/div[11]/button').click()