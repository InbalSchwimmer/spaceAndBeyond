import os
import allure
import pytest
from selenium import webdriver
from utills.config import ConfigReader


# Capture screenshot on test failure
def pytest_exception_interact(report):
    if report.failed:
        allure.attach(body=pytest.driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)


# Setup driver as a fixture
@pytest.fixture(scope="class", autouse=True)
def setup(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.maximize_window()
    url = ConfigReader.read_config("general", "url")
    driver.get(url)
    pytest.driver = driver
    yield
    driver.quit()


# Session finish hook for allure report
def pytest_sessionfinish() -> None:
    environment_properties = {
        'browser': pytest.driver.name,
        'driver_version': pytest.driver.capabilities['browserVersion']
    }
    allure_env_path = os.path.join("allure-results", 'environment.properties')
    with open(allure_env_path, 'w') as f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        f.write(data)
