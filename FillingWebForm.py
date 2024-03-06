# Filling the Web Form
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By  
import time
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains 
 

driver = webdriver.Chrome()
form_url = "https://iqssdss2020.pythonanywhere.com/tutorial/form/search"
driver.get(form_url)

element = driver.find_element(By.ID,'search_name').send_keys("A")
time.sleep(2)



element = driver.find_element(By.ID,'p5').click()
time.sleep(2)

element = driver.find_element(By.ID,"privacypolicy").click()
element = Select(driver.find_element(By.ID,"search_grade")).select_by_visible_text("5")
time.sleep(2)
element = driver.find_element(By.ID,"termsconditions").click()

element = driver.find_element(By.ID,"search").click()
time.sleep(2)

# create action chain object 
action = ActionChains(driver) 
  
# click the item 
action.click(on_element = element) 
  
# release the item 
action.release(on_element = element) 
  
# perform the operation 
action.perform() 