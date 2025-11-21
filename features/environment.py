import time

from selenium import webdriver

from Utilities import ConfigReader


# def before_all(context):
#     print("Starting test execution: opening browser")
#     context.driver1=webdriver.Chrome()
#     context.driver1.maximize_window()
#     time.sleep(2)
#
# def after_all(context):
#     print("Starting test execution: opening browser")
#     context.driver1.close()


def before_scenario(context, scenario):
   print("Starting test execution: opening browser")

   browserName=ConfigReader.read_configuration("basic info","browser")

   if browserName=="chrome":
       context.driver = webdriver.Chrome()
   elif browserName=="firefox":
       context.driver = webdriver.Firefox()
   elif browserName=="edge":
       context.driver = webdriver.Edge()
   context.driver.maximize_window()




def after_scenario(context, scenario):
   print("Starting test execution: opening browser")
   time.sleep(2)
   context.driver.close()




# def before_step(context, step):
#     print(f"Starting step:")
#
# def after_step(context, step):
#     print(f"Finished step:")
