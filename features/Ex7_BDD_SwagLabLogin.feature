Feature: Login to the SwagLab application
  Scenario: Login to app without Test Data
    Given User is on the Login page
    When User enter "standard_user"the Username
    And User enter "secret_sauce"the Password
    And User click the Login Button
    Then user should be on the HomepPage "Text1"