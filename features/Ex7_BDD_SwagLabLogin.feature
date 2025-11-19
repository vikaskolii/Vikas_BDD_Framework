Feature: Login to the SwagLab application


  Scenario: Login to app without Test Data
    Given User is on the Login page
    When User enter "standard_user"the Username
    And User enter "secret_sauce"the Password
    And User click the Login Button
    Then user should be on the HomepPage "Text1"



  Scenario: Login to app Using Invalid Credentials
    Given User is on the Login page of SwagLab App
    When User enter username "standard_user"on Swaglab login page
    And User enter password "Viki124koli" Swaglab login page
    And User click the Login Button on the Swag lab login page
    Then error msg is visible