import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function')
def driversetup():
    #driver Setup
    driver_option = Options()
    driver_option.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=driver_option)
    driver.maximize_window()
    yield driver
    #driver Tear down
    driver.quit()