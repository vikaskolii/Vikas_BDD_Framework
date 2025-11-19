from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver  #This gives suggestion when we call selenium methods


class SwagLabLogin:

    def __init__(self,driver:WebDriver):
        # driver:WebDriver“driver is a Selenium WebDriver object” and autocomplete will start working.
        self.driver:WebDriver= driver

# __init__ is a constructor that runs automatically when you create an instance of the class.
# It takes a parameter driver, which refers to the Selenium WebDriver instance.
# self.driver = driver stores this WebDriver object inside the class so that it can be reused in other methods (like login actions).
#convert local object/variable into class object/variable


        self.usernameXpath="//input[@id='user-name']"
        self.pwdXpath="//input[@id='password']"
        self.LoginButtonXpath="//input[@id='login-button']"
        self.LoginfailedmsgXpath="//h3[contains(text(),'Username and password do not match')]"

    def inpAPPloginUN(self, UN):
        self.driver.find_element(By.XPATH,self.usernameXpath).send_keys(UN)

    def inpAPPloginPWD(self,PWD):
        self.driver.find_element(By.XPATH,self.pwdXpath).send_keys(PWD)

    def clickAPPloginBUTTON(self):
        self.driver.find_element(By.XPATH,self.LoginButtonXpath).click()

    def geterrMsgDisplayed(self):
        return self.driver.find_element(By.XPATH,self.LoginfailedmsgXpath).text

#this can be also done this
 # def geterrMsgDisplayed(self):
 #        result=self.driver.find_element(By.XPATH,self.LoginfailedmsgXpath).text
 #        return result

