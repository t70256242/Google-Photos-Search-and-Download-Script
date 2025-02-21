from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import SessionNotCreatedException

download_dir = r"C:\Users\AY\Downloads"


options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_dir}
options.add_experimental_option("prefs", prefs)
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/recaptcha/api2/demo")

driver.maximize_window()
price = driver.find_element(By.XPATH,"//div[@class='g-recaptcha']")
price_content = price.get_attribute('innerHTML')
start = str(price_content).find(";k=") + len(";k=")
end = str(price_content).find("&amp;co")
driver.implicitly_wait(20)
driver.execute_script("document.getElementById('g-recaptcha-response').style.display = '';")
recaptcha_text_area = driver.find_element(By.ID, "g-recaptcha-response")

recaptcha_text_area.clear()
recaptcha_text_area.send_keys(price_content[start:end])
# .....................................................................................

button = driver.find_element(By.ID, "recaptcha-demo-submit")
