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
        self.addtoCartBtn="//button[@name='add-to-cart-sauce-labs-backpack']"
        self.removeBtnVisibleOrNot="(//button['@id=remove-sauce-labs-backpack'])[1]"

    def getAPPtext(self):
        actLogoText = self.driver.find_element(By.XPATH, self.getTextXpath).text
        return actLogoText

    def ClickaddtoCartBtn(self):
        self.driver.find_element(By.XPATH, self.addtoCartBtn).click()


    def GetremoveBtnVisibleOrNot(self):
      actResult=self.driver.find_element(By.XPATH, self.removeBtnVisibleOrNot).is_displayed()
      return actResult

