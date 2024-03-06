from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# Create a new instance of the WebDriver
driver = webdriver.Chrome()
# Open a website
driver.get("https://intellipaat.com/")
# Set the maximum amount of time to wait
timeout = 10
try:
    # Create a FluentWait instance with a timeout and polling interval
    wait = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.ID, "myElement"))
    )
    # Perform an action on the element after it becomes visible
    wait.click()
    # Print a success message
    print("Element is visible and clicked!")
except TimeoutException:
    # Print an error message if the element is not found within the timeout
    print("Timed out waiting for element to be visible!")
finally:
    # Close the browser
    driver.quit()

