from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  
   
def indeed_job_search():
    browser = webdriver.Chrome()
    browser.get('https://in.indeed.com/')
    browser.implicitly_wait(2) 
    search_bar = browser.find_element('id','text-input-what')
    search_bar.send_keys('Web Developer')
    search_bar.send_keys(Keys.RETURN)
    browser.implicitly_wait(2) 
    
    search_results = browser.find_elements(By.XPATH,'//h2/a')
 
    file = open("job_search.txt", 'a')
    file.write("\n")

    for job_element in search_results:
        job_title = job_element.text
        job_link = job_element.get_attribute('href')
        file.write("%s | link: %s \n" %(job_title, job_link))
 
    browser.close()
 
if __name__ == "__main__":
    indeed_job_search()
    