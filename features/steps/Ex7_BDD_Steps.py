import time
from behave import given, when, then

from features.pages import Home
from features.pages.Home import SwagLabHomepage
from features.pages.Login import SwagLabLogin


@given(u'User is on the Login page')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")

@when(u'User enter "{username}"the Username')
def step_impl(context,username):
    context.login = SwagLabLogin(context.driver)
    context.login.inpAPPloginUN(username)
    time.sleep(2)

@when(u'User enter "{password}"the Password')
def step_impl(context,password ):
    context.login = SwagLabLogin(context.driver)
    context.login.inpAPPloginPWD(password)
    time.sleep(2)

@when(u'User click the Login Button')
def step_impl(context):
    context.login.clickAPPloginBUTTON()

@then(u'user should be on the HomepPage "{expLogoText}"')
def step_impl(context,expLogoText):
    context.home = SwagLabHomepage(context.driver)
    actLogoText = context.home.getAPPtext()
    assert actLogoText == actLogoText, f"Failed act={actLogoText} & exp={expLogoText}"
