import time
from behave import when, then
from features.pages.Home import SwagLabHomepage

@when(u'User wait for "{timeinsec}" sec')
def step_impl(context,timeinsec):
    time.sleep(int(timeinsec))

@when(u'User add the one product in the cart')
def step_impl(context):
    context.home=SwagLabHomepage(context.driver)
    context.home.ClickaddtoCartBtn()

@then(u'User see the Remove Button')
def step_impl(context):
    actResult=context.home.GetremoveBtnVisibleOrNot()
    assert actResult ,"Failed-Remove btn is not visible"


