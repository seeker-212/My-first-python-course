from selenium import webdriver
from selenium.webdriver.chrome.service import Service

cdp = r'C:\Users\Pega\Desktop\driver\chromedriver-win64\chromedriver.exe'

service = Service(cdp)

driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com')

driver.quit()
