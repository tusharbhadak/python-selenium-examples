# Scrape tables
from selenium import webdriver
import time
from selenium.webdriver.common.by import By  

driver = webdriver.Chrome()
table_url = "https://iqssdss2020.pythonanywhere.com/tutorial/default/dynamic"
driver.get(table_url)
time.sleep(2)

file = open('scrape_tables.csv', "w", encoding = "utf-8")
table_body = driver.find_element(By.XPATH,'//*[@id="result"]/table/tbody')
entries = table_body.find_elements(By.TAG_NAME,'tr')

headers = entries[0].find_elements(By.TAG_NAME,'th')

table_header = ''
for i in range(len(headers)):
    header = headers[i].text
    if i == len(headers) - 1:
        table_header = table_header + header + "\n"
    else:
        table_header = table_header + header + ","
file.write(table_header)

for i in range(1, len(entries)):
    cols = entries[i].find_elements(By.TAG_NAME,'td')
    table_row = ''
    for j in range(len(cols)):
        col = cols[j].text
        if j == len(cols) - 1:
            table_row = table_row + col + "\n"
        else:
            table_row = table_row + col + ","
    file.write(table_row)


driver.close()
file.close()