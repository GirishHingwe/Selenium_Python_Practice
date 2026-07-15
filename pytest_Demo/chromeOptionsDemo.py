from selenium import webdriver
from selenium.webdriver.chrome.options import Options


try:
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    print("Title:", driver.title)

    driver.quit()

except Exception as e:
    print(e)