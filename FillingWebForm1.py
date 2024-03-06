# Filling the Web Form
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By  
import time
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains 
 

driver = webdriver.Chrome()
form_url = "https://internshala.com/"
driver.get(form_url)

element = driver.find_element(By.LINK_TEXT,'Hire Talent').click()
time.sleep(2)

element = driver.find_element(By.ID,'email').send_keys("pqr@gmail.com")
time.sleep(2)

element = driver.find_element(By.ID,'password').send_keys("Abc@123")
time.sleep(2)

element = driver.find_element(By.NAME,"first_name").send_keys("Abc")
time.sleep(2)

element = driver.find_element(By.NAME,"last_name").send_keys("Xyz")
time.sleep(2)

element = driver.find_element(By.NAME,"phone_primary").send_keys("9087604563")
time.sleep(2)

element = driver.find_element(By.ID,"job_employer_registration_button").click()
time.sleep(2)

# create action chain object 
action = ActionChains(driver) 
  
# click the item 
action.click(on_element = element) 
  
# release the item 
action.release(on_element = element) 
  
# perform the operation 
action.perform() 