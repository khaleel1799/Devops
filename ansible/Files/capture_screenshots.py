from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

departments = {
    "marketing": "http://192.168.73.128:8080/",
    "sales": "http://192.168.73.128:7001/console"
}

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1200x800")

driver = webdriver.Chrome(options=options)

for dept, url in departments.items():
    driver.get(url)
    sleep(3)  # wait for page load
    driver.save_screenshot(f"screenshots/{dept}.png")

driver.quit()
