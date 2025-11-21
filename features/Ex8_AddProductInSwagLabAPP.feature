Feature: Add product
  Scenario: User should add product in the cart
    Given User is on the Login page
    When User enter "standard_user"the Username
    And User wait for "2" sec
    And User enter "secret_sauce"the Password
    And User wait for "2" sec
    And User click the Login Button
    And User wait for "2" sec
    And User add the one product in the cart
    And User wait for "2" sec
    Then User see the Remove Button