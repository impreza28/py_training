from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAddGroup():
  def setup_method(self, method):
    self.wd = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.wd.quit()
  
  def test_add_group(self):
    self.wd.get("http://localhost/addressbook/")
    self.wd.set_window_size(2062, 1126)
    self.wd.find_element(By.NAME, "user").send_keys("admin")
    self.wd.find_element(By.NAME, "pass").send_keys("secret")
    self.wd.find_element(By.XPATH, "//input[@value=\'Login\']").click()
    self.wd.find_element(By.LINK_TEXT, "groups").click()
    self.wd.find_element(By.NAME, "new").click()
    self.wd.find_element(By.NAME, "group_name").send_keys("test")
    self.wd.find_element(By.NAME, "group_header").send_keys("test1")
    self.wd.find_element(By.NAME, "group_footer").send_keys("test2")
    self.wd.find_element(By.NAME, "submit").click()
    self.wd.find_element(By.LINK_TEXT, "group page").click()
    self.wd.find_element(By.LINK_TEXT, "Logout").click()
  
