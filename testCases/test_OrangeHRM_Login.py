import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import LoginPage_Class
from utilities.LoggerFile import LogGenerator
from utilities.readConfigFile import ReadConfig_Class


class Test_OrangeHRM_Login:
    Username = ReadConfig_Class.getUsername()
    Password = ReadConfig_Class.getPassword()
    log = LogGenerator.loggen()

    @allure.title("URL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_OrangeHRM_url_001(self, setup):
        # self.log.debug("this is debug")
        # self.log.info("this is info")
        # self.log.warning("this is warning")
        # self.log.error("this is error")
        # self.log.critical("this is critical")
        self.log.info("test_OrangeHRM_url_001 is started")
        self.driver = setup
        self.log.info("Opening Browser")
        print("driver.title-->" + self.driver.title)
        self.log.info("Verifying the page title")
        if self.driver.title == "OrangeHRM":
            self.log.info("test_OrangeHRM_url_001 is passed, user is landed on correct url")
            time.sleep(2)
            self.log.info("Taking the screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_url_001_pass.png")
            assert True
        else:
            self.log.info("test_OrangeHRM_url_001 is failed")
            self.log.info("Taking the screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_url_001_fail.png")
            assert False

        self.log.info("Closing the Browser")
        self.driver.quit()
        self.log.info("test_OrangeHRM_url_001 is completed")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_OrangeHRM_Login_002(self, setup):
        self.log.info("test_OrangeHRM_Login_002 is started")
        self.driver = setup
        self.log.info("Opening the browser")
        self.lp = LoginPage_Class(self.driver)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        #print("Username-->" + self.Username)
        #print("Password-->" + self.Password)
        self.log.info("Entering Username-->" + self.Username)
        self.lp.Enter_UserName(self.Username)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.log.info("Entering Password-->" + self.Password)
        self.lp.Enter_Password(self.Password)
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.log.info("Clicking on login button")
        self.lp.Click_LoginButton()
        self.log.info("Verifying the login stauts")
        if self.lp.Validate_Login_Stauts() == "LoginPass":
            self.log.info("test_OrangeHRM_Login_002 is passed")
            time.sleep(2)
            self.log.info("Taking the screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_002_pass.png")
            self.log.info("Clicking on Menu button")
            self.lp.Click_Menu_Button()
            self.log.info("Clicking on logout button")
            self.lp.Click_Logout_Button()
            assert True
        else:
            self.log.info("test_OrangeHRM_Login_002 is failed")
            self.log.info("Taking for screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_002_fail.png")
            assert False
        self.log.info("Closing the browser")
        self.driver.quit()
        self.log.info("test_OrangeHRM_Login_002 is Completed")

# Pytest -v -s --html=HTMLReports/myreport.html --allure="AllureReports" -n=4 -m -k
# generally in automation  as a tester we have to capture screenshots for fail case

# screenshots in other ways--> assignment , specific area portion screenshot capture
