import time
from pageObjects.addcustomerpage import Registration
from pageObjects.custSearchPage import custSearchPage
from pageObjects.loginPage import login
from utilities.readproperties import Readconfig

class Test_003:
    baseurl = Readconfig.getApplicationurl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()

    def test_searchByEMail(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.obj = login(self.driver)
        self.obj.setusername(self.username)
        self.obj.setpassword(self.password)
        self.obj.clicklogin()
        self.obj2 = Registration(self.driver)
        self.obj2.clickoncustomermenu()
        self.obj2.clickoncustomeritem()
        self.obj3 = custSearchPage(self.driver)
        email = "admin@yourStore.com"
        self.obj3.test_search_by_email(email)
        self.obj3.test_btn_click()

    def test_SearchByName(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.obj = login(self.driver)
        self.obj.setusername(self.username)
        self.obj.setpassword(self.password)
        self.obj.clicklogin()
        self.obj2 = Registration(self.driver)
        self.obj2.clickoncustomermenu()
        self.obj2.clickoncustomeritem()
        self.obj3 = custSearchPage(self.driver)








