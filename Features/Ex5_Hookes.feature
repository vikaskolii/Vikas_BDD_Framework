Feature: Login to application
 Scenario: login to app with valid credentials
   Given user open browser
   When user enter url
   And user enter username
   And user enter password
   And user click on login btn
   Then user should be at home page


 Scenario: login to app with invalid credentials
   Given user open browser
   When user enter url
   And user enter invalid username
   And user enter invalid password
   And user click on login btn
   Then user can see error msg

   Scenario: To Succesful Login into the website
    Given User have to enter the Correct URL
    When User enter the name
    And user enter the surname
    And User enter the Mail-id
    And User enter the Password
    And User click the Submit Button
    Then User enter in the Websites Homepage