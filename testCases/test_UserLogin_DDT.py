import time
import openpyxl
from selenium import  webdriver
from pageObjects.LoginPage import LoginPageClass
from utilities import ExcelMethod


class Test_UserLogin_DDT:
    Excel_File_Path = "F:\\STUDY\\Credence IT\\nopcom_pytest_project\\TestData\\Book1.xlsx"

    def test_UserLogin_DDT_005(self, setup):
        self.driver = setup

        self.l = LoginPageClass(self.driver)

        self.rows = ExcelMethod.numRows(self.Excel_File_Path , 'Sheet1' ) # providing file and sheet name
        print("number of rows in Excel sheet ",self.rows)

        test_results = []

        for r in range(2, self.rows+1): # ignore the header start with 2nd row (2,6) means row num 2,3,4,5
            self.username = ExcelMethod.readData(self.Excel_File_Path,"Sheet1", r, 1)
            self.password = ExcelMethod.readData(self.Excel_File_Path,"Sheet1", r, 2)
            self.expected_result = ExcelMethod.readData(self.Excel_File_Path,"Sheet1", r, 3)
            print("Iteration / Row number ", r)
            print("Username --> ", self.username)
            print("Password --> ", self.password)
            print("\n")

            time.sleep(3)

            self.l.Enter_Email(self.username)
            time.sleep(1)
            self.l.Enter_Password(self.password)
            time.sleep(1)
            self.l.Click_Login()

            if (self.l.Login_Verify_Status() == "Pass" and self.expected_result == "Pass") :
                ExcelMethod.writeData(self.Excel_File_Path,"Sheet1", r, 4, "Pass")
                test_results.append("Pass")
                time.sleep(5)
                self.l.Click_Logout()

            elif (self.l.Login_Verify_Status() == "Fail" and self.expected_result == "Fail"):
                ExcelMethod.writeData(self.Excel_File_Path,"Sheet1", r, 4, "Fail")
                test_results.append("Pass")

            else:
                test_results.append("Fail")

        print("List test results is --> ",test_results)


        if "Fail" in test_results:
            print("Test Case test_UserLogin_DDT_005 is Failed ")
            assert False
        else:
            print("Test Case test_UserLogin_DDT_005 is Passed ")
            assert True






