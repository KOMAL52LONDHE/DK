import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import LoginPage_Class
from utilities.LoggerFile import LogGenerator
from utilities.readConfigFile import ReadConfig_Class

class Test_OrangeHRM_Login_params:
    log = LogGenerator.loggen()

    def test_OrangeHRM_Login_params_003(self, setup, getDataForLogin):
        self.log.info("test_OrangeHRM_Login_params_003 is started")
        self.driver = setup
        self.log.info("Opening the browser")
        self.lp = LoginPage_Class(self.driver)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        #print("Username-->" + self.Username)
        #print("Password-->" + self.Password)
        self.log.info("Entering Username-->" + getDataForLogin[0])
        self.lp.Enter_UserName(getDataForLogin[0])
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.log.info("Entering Password-->" + getDataForLogin[1])
        self.lp.Enter_Password(getDataForLogin[1])
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.log.info("Clicking on login button")
        self.lp.Click_LoginButton()
        self.log.info("Verifying the login stauts")
        if self.lp.Validate_Login_Stauts() == "LoginPass" and getDataForLogin[2] == "Login_Pass" :
            self.log.info("test_OrangeHRM_Login_params_003 is passed")
            time.sleep(2)
            self.log.info("Taking the screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_003_pass.png")
            self.log.info("Clicking on Menu button")
            self.lp.Click_Menu_Button()
            self.log.info("Clicking on logout button")
            self.lp.Click_Logout_Button()
            assert True
        elif self.lp.Validate_Login_Stauts() == "LoginPass" and getDataForLogin[2] == "Login_Fail" :
            self.log.info("test_OrangeHRM_Login_params_003 is failed")
            self.log.info("Taking for screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_003_fail.png")
            self.log.info("Clicking on Menu button")
            self.lp.Click_Menu_Button()
            self.log.info("Clicking on logout button")
            self.lp.Click_Logout_Button()
            assert False
        elif self.lp.Validate_Login_Stauts() == "LoginFail" and getDataForLogin[2] == "Login_Pass" :
            self.log.info("test_OrangeHRM_Login_params_003 is failed")
            self.log.info("Taking for screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_003_fail.png")
            assert False

        elif self.lp.Validate_Login_Stauts() == "LoginFail" and getDataForLogin[2] == "Login_Fail" :
            self.log.info("test_OrangeHRM_Login_params_003 is failed")
            self.log.info("Taking for screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_003_fail.png")
            assert True
        self.log.info("Closing the browser")
        self.driver.quit()
        self.log.info("test_OrangeHRM_Login_params_003 is Completed")
