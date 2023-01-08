import pytest
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

test_list = ['236895',
             '236896',
             '236897',
             '236898',
             '236899',
             '236903',
             '236904',
             '236905']


def ans():
    answer = math.log(int(time.time()))
    return answer


@pytest.mark.parametrize('num', test_list)
class TestAuthorization:

    def test_authorization(self, get_webdriver, num):
        self.driver = get_webdriver
        self.wait = WebDriverWait(self.driver, 15)
        self.link = f'https://stepik.org/lesson/{num}/step/1'

        # print your e-mail
        self.email = ''
        # print your password
        self.psw = ''

        self.driver.get(self.link)
        self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a#ember33'))).click()
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#id_login_email'))).send_keys(self.email)
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#id_login_password'))).send_keys(self.psw)
        self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button.sign-form__btn'
                                                                     '.button_with-loader '))).click()
        time.sleep(4)  #need to use this because of page's problems
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                          '.ember-text-area.ember-view.textarea'
                                                          '.string-quiz__textarea'))).clear()
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                          '.ember-text-area.ember-view.textarea'
                                                          '.string-quiz__textarea'))).send_keys(str(ans()))
        self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission'))).click()
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'p.smart-hints__hint')))
        self.feedback = self.driver.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint').text
        assert self.feedback == "Correct!", f'Must be \'Correct!\', not \'{self.feedback}\' '
