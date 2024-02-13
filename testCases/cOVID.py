import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities import ExcelMethod

class Test_Covid_Count:
    driver = webdriver.Chrome()
    driver.get("https://www.mygov.in/covid-19/")
    driver.maximize_window()
    excel_file_path = "F:\\STUDY\\Credence IT\\nopcom_pytest_project\\TestData\\Book1.xlsx"

    def test_covid_state_wise_count_up(self):

        self.driver.find_element(By.XPATH, "//a[@title='Click to Expand COVID-19 Statewise Status']").click()
        time.sleep(5)
        rowCount = len(self.driver.find_elements(By.XPATH, "//table[@id='ind_mp_tbl']/tbody/tr"))
        print("rowCount ", rowCount)

        row_num = 2

        for r in range(1, rowCount + 1):
            try:
                states_case_change_count = self.driver.find_element(By.XPATH, "//table[@id='ind_mp_tbl']/tbody/tr[" + str(r) + "]/td[3]/p/span").text

                if int(states_case_change_count) >= 2 :

                    state = self.driver.find_element(By.XPATH, "//table[@id='ind_mp_tbl']/tbody/tr["+str(r)+"]/td[1]").text
                    states_case_change_count = self.driver.find_element(By.XPATH, "//table[@id='ind_mp_tbl']/tbody/tr["+str(r)+"]/td[3]/p/span").text
                    print("state is : "+state+" & change in cases "+states_case_change_count)
                    time.sleep(2)
                    ExcelMethod.writeData(self.excel_file_path, "Sheet2", row_num,1, str(state))
                    ExcelMethod.writeData(self.excel_file_path, "Sheet2", row_num,2, str(states_case_change_count))
                    row_num += 1
            except:
                pass














