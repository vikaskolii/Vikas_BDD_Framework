from behave import given, when, then

@given("user open browser")
def step_impl(context):
    print("Browser opened")

@when("user enter url")
def step_impl(context):
    print("URL entered")

@when("user enter username")
def step_impl(context):
    print("Username entered")

@when("user enter password")
def step_impl(context):
    print("Password entered")

@when("user click on login btn")
def step_impl(context):
    print("Login button clicked")

@then("user should be at home page")
def step_impl(context):
    print("Landed on Home page")



@when("user enter invalid username")
def step_impl(context):
    print("Invalid username")

@when("user enter invalid password")
def step_impl(context):
    print("Invalid password")

@then("user can see error msg")
def step_impl(context):
    print("Error message shown")





@given('User have to enter the Correct URL')
def step_impl(context):
    print('Given User have to enter the Correct URL')


@when('User enter the name')
def step_impl(context):
    print('When User enter the name')


@when('user enter the surname')
def step_impl(context):
    print('When user enter the surname')


@when('User enter the Mail-id')
def step_impl(context):
    print('When User enter the Mail-id')


@when('User enter the Password')
def step_impl(context):
   print ('When User enter the Password')


@when('User click the Submit Button')
def step_impl(context):
   print('When User click the Submit Button')


@then('User enter in the Websites Homepage')
def step_impl(context):
   print('Then User enter in the Websites Homepage')