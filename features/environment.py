import time

from behave import *
from selenium import webdriver


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
   context.driver=webdriver.Chrome()
   context.driver.maximize_window()
   context.driver.get("https://www.saucedemo.com/")
   time.sleep(5)


def after_scenario(context, scenario):
   print("Starting test execution: opening browser")
   time.sleep(2)
   context.driver.close()




# def before_step(context, step):
#     print(f"Starting step:")
#
# def after_step(context, step):
#     print(f"Finished step:")
