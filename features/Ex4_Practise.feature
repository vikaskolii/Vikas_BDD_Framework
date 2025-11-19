Feature: Login website
  Scenario: To Succesful Login into the website
    Given User have to enter the Correct URL
    When User enter the name
    And user enter the surname
    And User enter the Mail-id
    And User enter the Password
    And User click the Submit Button
    Then User enter in the Websites Homepage
