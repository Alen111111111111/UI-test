import time
from selenium import webdriver

driver = webdriver.Edge(executable_path = "msedgedriver.exe")

driver.get("http://suninjuly.github.io/simple_form_find_task.html")

start = time.time()
textarea1 = driver.find_element_by_css_selector(".form-group:first-child>input")
textarea1.send_keys("name")

textarea2 = driver.find_element_by_css_selector(".form-group:nth-child(2)>input")
textarea2.send_keys("last name")

textarea3 = driver.find_element_by_css_selector(".form-group:nth-child(3)>input")
textarea3.send_keys("city")

textarea4 = driver.find_element_by_css_selector(".form-group:nth-child(4)>input")
textarea4.send_keys("Country")

submit_button = driver.find_element_by_css_selector("#submit_button")

submit_button.click()

print("Время выполнения:", 	time.time() - start)

