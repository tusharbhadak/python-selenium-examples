# import webdriver 
from selenium import webdriver 
from selenium.webdriver.common.by import By  
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains 
 
driver = webdriver.Firefox() 

# get geeksforgeeks.org 
driver.get("https://www.geeksforgeeks.org/") 

# get element 
element = driver.find_element(By.LINK_TEXT,"Python") 

# create action chain object 
action = ActionChains(driver) 
  
# click the item 
action.click(on_element = element) 
  
# release the item 
action.release(on_element = element) 
  
# perform the operation 
action.perform() 