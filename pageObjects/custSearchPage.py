from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class custSearchPage:
    textbox_email_id = (By.XPATH,"//input[@id='SearchEmail']")
    textbox_firstname_id = (By.XPATH,"//input[@id='SearchFirstName']")
    testbox_lastname_id = (By.XPATH,"//input[@id='SearchLastName']")
    btn_search_id = (By.XPATH,"//button[@id='search-customers']")
    data_table = (By.XPATH,'//*[@id="customers-grid"]')
    result_search_table = (By.XPATH,'//*[@id="customers-grid_wrapper"]/div[1]')
    table_row_xpath = (By.XPATH,'//*[@id="customers-grid"]/tbody/tr')
    table_column_xpath = (By.XPATH,'//*[@id="customers-grid"]/tbody/tr/td')

    def search_cust_by_email(self,email):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH,self.data_table)
            empid = table.find_element(By.XPATH,'//*[@id="customers-grid"]/tbody/tr['+str(r)+'/td[2]').text
            print(empid)
            if email == empid:
                flag = True
                break
        return flag




    def __init__(self,driver):
        self.driver = driver

    def test_search_by_email(self,email):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.textbox_email_id)).send_keys(email)

    def test_btn_click(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.btn_search_id)).click()




