from selenium import webdriver
from selenium.webdriver.common.by import By
# time.sleep() function is required because selenium needs a page to be fully loaded first otherwise errors may occur
import time
# Usage time.sleep(x) Where x is time in seconds and may vary according to your connection

# I have made class so that extra methods can be added later on if required
class instagramBot:
	def __init__(self, username, password):
		# these lines will help if someone faces issues like chrome closes after execution
		self.opts = webdriver.ChromeOptions()
		self.opts.add_experimental_option("detach", True)
		self.driver = webdriver.Chrome(options=self.opts)

		# Username and password
		self.username = username
		self.password = password

		# Opens Instagram login page
		self.driver.get("https://instagram.com")
		time.sleep(2) # 1 Second Wait

		# Automatically enters your username and password to instagram's username field
		self.driver.find_element(
			By.XPATH, "//input[@name = 'username']").send_keys(self.username)
		self.driver.find_element(
			By.XPATH, "//input[@name = 'password']").send_keys(self.password)

		# Clicks on Log In Button
		self.driver.find_element(
			By.XPATH, "//div[contains(text(), 'Log in')]").click()
		time.sleep(2)

		# Bonus: Automatically clicks on 'Not Now' when Instagram asks to show notifications
		self.driver.find_element(
			By.XPATH, "//button[contains(text(), 'Not Now')]").click()

# Testing Your Code
instagramBot('Sample Username', 'Sample Password')
