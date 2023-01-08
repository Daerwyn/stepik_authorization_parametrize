import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_options

@pytest.fixture
def get_options():
    options = Chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start_maximized')
    return options

@pytest.fixture
def get_webdriver(get_options):
    options = get_options
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()