

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="F://chromedriver_win//chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(3)
driver.maximize_window()

driver.find_element_by_id("txtUsername").send_keys("Admin")

driver.find_element(By.ID,"txtPassword").send_keys("admin123")

driver.find_element(By.ID,"btnLogin").click()
time.sleep(3)

driver.find_element(By.LINK_TEXT,"PIM").click()
driver.find_element(By.XPATH,"//*[@id='empsearch_employee_name_empName']").send_keys("Amol")
driver.find_element(By.ID,"empsearch_id").send_keys("0227")
l=driver.find_element(By.XPATH,"//*[@id='empsearch_employee_status']")
drp= Select(l)
drp.select_by_index(3)
print(len(drp.options))

all_options=drp.options
for option in all_options:
    print(option.text)


m=driver.find_element(By.XPATH,"//*[@id='empsearch_termination']")
drp= Select(m)
drp.select_by_visible_text("Current and Past Employees")
print(len(drp.options))

all_options=drp.options
for option in all_options:
    print(option.text)

