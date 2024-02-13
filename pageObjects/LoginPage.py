import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPageClass:
    Text_Email_XPATH = "//input[@id='Email']"
    Text_Password_XPATH = "//input[@id='Password']"
    Click_LoginButton_XPATH = "//button[normalize-space()='Log in']"
    Click_LogoutButton_XPATH = "//a[normalize-space()='Logout']"


    def __init__(self,driver):
        self.driver=driver # received from test_UserLogin
        self.wait = WebDriverWait(self.driver, 3)   # task poll frequency # default poll frequency


    def Enter_Email(self,email):
        self.driver.find_element(By.XPATH,self.Text_Email_XPATH).clear() # to clear already written text in the field
        self.driver.find_element(By.XPATH,self.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self,password):
        self.driver.find_element(By.XPATH,self.Text_Password_XPATH).clear()
        self.driver.find_element(By.XPATH,self.Text_Password_XPATH).send_keys(password)


    def Click_Login(self):
        self.driver.find_element(By.XPATH,self.Click_LoginButton_XPATH).click()


    def Click_Logout(self):
        self.driver.find_element(By.XPATH,self.Click_LogoutButton_XPATH).click()


    def Login_Verify_Status(self):

        try: # we write such code which may cause an exception like ElementNotIteracable
            self.driver.find_element(By.XPATH, self.Click_LogoutButton_XPATH) # if logout button xpath is present means login is successful

            return "Pass"


        except:
            return "Fail"

