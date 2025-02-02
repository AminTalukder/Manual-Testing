from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()  
driver.get("https://the-internet.herokuapp.com/login")  # Test website

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

time.sleep(5)
driver.quit()
