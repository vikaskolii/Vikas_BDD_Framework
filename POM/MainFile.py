import time
from selenium import webdriver

from features.pages import Login, Home

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

#Here we call constructor Login()---->POM-1

login=Login.SwagLabLogin(driver)
login.inpAPPloginUN("standard_user")
login.inpAPPloginPWD("secret_sauce")
login.clickAPPloginBUTTON()
time.sleep(3)

#Here we call constructor Homepage()---->POM-2
home=Home.SwagLabHomepage(driver)

actLogoText=home.getAPPtext()
expLogoText = "Swag Labs"

assert actLogoText == expLogoText, "FAILED: Logo text does not match"


# if actLogoText==expLogoText:
#     print("PASS")
# else:
#     print("FAIL")

time.sleep(3)
driver.quit()




