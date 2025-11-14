Feature: Login to app
  Scenario: Login to app without Test data
    Given User enter the URL
    And user enter the username
    And user enter the Password
    And user click the submit Button
    Then User is on the Homepage