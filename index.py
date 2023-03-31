import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Set up session and login information
session = requests.Session()
login_url = "http://gruposm.dyndns.org:3306/SST/Account/Login.aspx"
username = "gsmadmin"
password = "202120"

# Use selenium to launch a browser and navigate to the login page
browser = webdriver.Chrome()
browser.get(login_url)

# Wait for the page to load
wait = WebDriverWait(browser, 5)




username_field = browser.find_element("xpath", "//input[@id='txtUsuario_I']")
password_field = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.NAME, "password")))

time.sleep(5)  # Wait for 5 seconds

username_field.send_keys(username)
password_field.send_keys(password)

# Submit the login form
submit_button = browser.find_element("xpath", "//input[@id='btnIngresar_I']")
submit_button.click()

# Get the cookies from the browser and add them to the session
cookies = browser.get_cookies()
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])

# Use requests to access a protected page on the website and extract data
protected_page_url = "http://gruposm.dyndns.org:3306/SST/Custodia/CustodiaCargaFinal.aspx"
response = session.get(protected_page_url)
soup = BeautifulSoup(response.content, 'html.parser')

while True:
    # Find the button element on the webpage using its XPath expression
    button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[5]/table[3]/tbody/tr/td/div[1]/table/tbody/tr/td[1]/div/div/img")))

    # Click the button
    button.click()

    # Wait for 60 seconds before clicking the button again
    time.sleep(60)

# Wait for user input before closing the browser
input("Press Enter to close the browser...")
browser.quit()






