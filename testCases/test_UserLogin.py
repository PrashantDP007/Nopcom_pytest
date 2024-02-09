import time

import pytest
from selenium import webdriver

from pageObjects.LoginPage import LoginPageClass

from utilities.readconfigfile import Readconfig
from utilities.Logger import LogGenerator

@pytest.mark.usefixtures("setup")
class Test_Login:
    Email = Readconfig.getEmail()
    Password = Readconfig.getPassword()
    log = LogGenerator.log_gen()


    def test_verify_url001(self,setup):
        self.log.info("test case test_verify_url001 started ")
        self.driver = setup

        time.sleep(2)
        self.log.info("Opening browser and navigating to demnopcommerce ")
        # self.log.info("Page time is --> ", self.driver.title)
        print(self.driver.title)

        time.sleep(2)
        # self.log.warning("")
        # self.log.critical("")
        # self.log.error("")


        if self.driver.title == "Your store. Login":
            self.log.info("test case test_verify_url001 is Passed")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot("..\\Screenshots\\test_verify_url001_pass.png")
            assert True
        else:
            self.log.info("test case test_verify_url001 is Failed")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot("..\\Screenshots\\test_verify_url001_fail.png")

            assert False
        self.log.info("test case test_verify_url001 Completed ")


    # def test_user_login002(self,setup):
    #     self.driver = setup
    #
    #     self.l = LoginPageClass(self.driver) # sending driver through constructor
    #     time.sleep(3)
    #     self.l.Enter_Email(self.Email)
    #     time.sleep(2)
    #     self.l.Enter_Password(self.Password)
    #     time.sleep(2)
    #     self.l.Click_Login()
    #     time.sleep(2)
    #
    #
    #     if self.l.Login_Verify_Status() == "Pass":
    #         self.driver.save_screenshot("..\\Screenshots\\test_User_login002_pass.png")
    #         time.sleep(2)
    #         # self.l.Click_Logout()
    #         assert True
    #     else:
    #         self.driver.save_screenshot("..\\Screenshots\\test_User_login002_fail.png")
    #         assert False



