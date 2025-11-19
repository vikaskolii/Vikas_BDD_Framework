# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webdriver import WebDriver  #This gives suggestion when we call selenium methods
#
#
# class SwagLabHomepage:
#
#     def __init__(self, driver: WebDriver):
#         # driver:WebDriver“driver is a Selenium WebDriver object” and autocomplete will start working.
#         self.driver: WebDriver = driver
#
#
#         self.getTextXpath = "//div[@class='app_logo']"
#
#     def getAPPtext(self,driver):
#         actLogoText=self.driver.find_element(By.XPATH, self.getTextXpath).text
#         return actLogoText
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class SwagLabHomepage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.getTextXpath = "//div[@class='app_logo']"

    def getAPPtext(self):
        actLogoText = self.driver.find_element(By.XPATH, self.getTextXpath).text
        return actLogoText
