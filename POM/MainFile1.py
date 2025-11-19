import time
from selenium import webdriver
from Login import SwagLabLogin
from Homepage import SwagLabHomepage
from POM import Login, Homepage

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

#Here we call constructor Login()---->POM-1

loginObj=Login.SwagLabLogin(driver)
loginObj.inpAPPloginUN("standard_user")
loginObj.inpAPPloginPWD("secret_sace")
loginObj.clickAPPloginBUTTON()
time.sleep(2)
actResult=loginObj.geterrMsgDisplayed()

if actResult:
    print("PASS- Error msg present")
else:
    print("FAIL- Error msg not present")
time.sleep(3)
driver.quit()




