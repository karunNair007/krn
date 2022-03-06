import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver


class Testpyk():

    @pytest.yield_fixture(scope="class")
    def test_parent(self):
        global driver
        driver=webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
        driver.maximize_window()
        time.sleep(4)
        yield
        driver.quit()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_first(self,test_parent):

        driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
        driver.find_element_by_xpath("//*[@name='sloginid']").send_keys("cdolman")
        driver.find_element_by_xpath("//*[@name='spassword']").send_keys("123")
        driver.find_element_by_xpath("//*[text()='Login']").click()
        allure.attach(driver.get_screenshot_as_png(),name="test",attachment_type=AttachmentType.PNG)
        time.sleep(4)


    def test_second(self,test_parent):
        pytest.skip("We are going to skip this test case")
        driver.find_element_by_xpath("//*[text()='Registration']").click()