# Test Suite for Login Form and Subsequent Actions
This test suite is meant for learning purposes and tests a login form and subsequent actions on a website. It includes a single test case, **TestAuthorization**, which is parameterized with a list of values.

The **test_authorization** method within **TestAuthorization** does the following:

- Navigates to a webpage
- Logs in with provided credentials
- Enters a value into a text field and submits it
- Verifies that the feedback received is correct

To use this test suite, you will need to provide your own email and password in the appropriate variables.

In addition to the test suite, this repository includes the **conftest.py** file, which contains fixtures for setting up and tearing down a Chrome webdriver. The **get_webdriver** fixture takes an optional **get_options** fixture, which can be used to customize the Chrome options. By default, the webdriver will be started maximized.
