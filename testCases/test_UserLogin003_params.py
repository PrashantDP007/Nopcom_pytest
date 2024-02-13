import time

import pytest
from selenium import webdriver

from pageObjects.LoginPage import LoginPageClass
from utilities.readconfigfile import Readconfig

@pytest.mark.usefixtures("setup","DataForLogin")
class Test_Login_Params:
    def test_user_login002(self, setup, DataForLogin):
        self.driver = setup

        self.l = LoginPageClass(self.driver) # sending driver through constructor
        time.sleep(3)
        self.l.Enter_Email(DataForLogin[0])
        time.sleep(2)
        self.l.Enter_Password(DataForLogin[1])
        time.sleep(2)
        self.l.Click_Login()
        time.sleep(2)

        print("Expected Result--> ",DataForLogin[2])

        # if DataForLogin[2] == "Pass":
        #     if self.l.Login_Verify_Status() == "Pass":
        # # actual reasult is pass and expected result(DataforLogin[2]) is pass so Test case is paased [Actual = Expected]
        #         assert True
        #     else:
        #         assert False
        # # actual reasult is failed and expected result(DataforLogin[2]) is pass so Test case is Fail
        #
        # else: # here expected result is fail
        #     if self.l.Login_Verify_Status() == "Pass":
        #         # actual reasult is pass and expected result(DataforLogin[2]) is Fail so Test case is Fail
        #         assert False
        #     else:
        #         assert True
        #     # actual reasult is failed and expected result(DataforLogin[2]) is Fail so Test case is Pass
        test_results = []

        if (self.l.Login_Verify_Status() == "Pass" and  DataForLogin[2] == "Pass" ):
            assert True
            test_results.append("Pass")
        elif (self.l.Login_Verify_Status() == "Fail" and  DataForLogin[2] == "Fail"):
            assert True
            test_results.append("Pass")
        else:
            test_results.append("Fail")
            assert False

        if "Fail" in test_results:
            print("test_UserLogin003_params is Passed")
        else:
            print("test_UserLogin003_params is Failed")








