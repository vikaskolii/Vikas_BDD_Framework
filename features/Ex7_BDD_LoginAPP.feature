Feature: Login to the SwagLab application
  Scenario: Login to app without Test Data
    Given User Open the Browser
    When User Enter URL
    And User enter the Username
    And User enter the Password
    And User click the Login Button
    Then user should be on the HomepPage