import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchElementException, TimeoutException,
                                        WebDriverException, StaleElementReferenceException,
                                        ElementNotInteractableException)
import requests
import base64
import os
import random


time_series = [6, 8, 9]
url = "https://www.google.com/"
player = input("Enter Player's Name? ")

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.google.com/",
    }

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--window-size=1280,800")
chrome_options.add_argument("--disable-gpu")

chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

print("Starting google photo search headless")
for i in range(3):
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        driver.get(url)
        time.sleep(4)
        break
    except (TimeoutException, NoSuchElementException, WebDriverException, Exception):
        if i < 2:
            print("Encountered an error. retrying........")
            time.sleep(3)
        else:
            print("Script failed, retry later........quiting")
            driver.quit()
            break


for i in range(3):
    try:
        search_bar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
        )
        search_bar.send_keys(f"{player} photos", Keys.ENTER)
        print("Search query entered and submitted.")

        image = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="hdtb-sc"]/div/div[1]/div[1]/div/div[2]/a/div'))
        )
        time.sleep(3)
        image.click()

        moc = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#search div div div div div"))
        )
        gOTY1 = WebDriverWait(moc, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div div div"))
        )
        final = WebDriverWait(gOTY1, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div"))
        )
        print("Found the image search result.")
        break

    except (NoSuchElementException, TimeoutException, StaleElementReferenceException,
            ElementNotInteractableException, Exception) as e:
        if i < 2:
            print(f"Error occurred: {e}.. retrying")
            time.sleep(10)
            driver.get(url)
            time.sleep(3)
        else:
            print("Script failed, retry later........quiting")
            driver.quit()
            break


count = 0
for em in final.find_elements(By.TAG_NAME, value="div"):
    try:

        if em.get_attribute("data-lpage") is None:
            continue

        image_a = WebDriverWait(em, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.XOEbc h3'))
        )
        image_a.click()

        anchor_ = WebDriverWait(image_a, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a'))
        )

        original_tab = driver.current_window_handle
        new_link = anchor_.get_attribute('href')

        for i in range(3):
            try:

                driver.execute_script(f"window.open('{new_link}', '_blank');")

                driver.switch_to.window(driver.window_handles[1])
                break
            except (TimeoutError, TimeoutException, Exception) as e:
                if i < 2:
                    driver.close()
                    driver.switch_to.window(original_tab)
                else:
                    print(f"❌ Image error. Message: {e}")
                    print("...continuing....")
                    driver.close()
                    time.sleep(3)
                    driver.switch_to.window(original_tab)
                    time.sleep(random.choice(time_series))
                    continue

        inner_a = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.PUxBg a img'))
        )

        image_src = inner_a.get_attribute('src')

        if image_src and image_src.startswith('data:image'):
            base64_data = image_src.split(',')[1]
            image_data = base64.b64decode(base64_data)
        else:
            try:
                response = requests.get(image_src, headers=headers)
                if response.status_code == 200:
                    image_data = response.content
                else:
                    print(f"❌ Failed to download image. Status code: {response.status_code}")
                    print("...continuing....")
                    driver.close()
                    driver.switch_to.window(original_tab)
                    continue
            except requests.RequestException as e:
                print(f"❌ Error downloading image: {e}")
                print("...continuing....")
                time.sleep(random.choice(time_series))
                driver.close()
                driver.switch_to.window(original_tab)
                continue

        file_name = f"{player}_download_{count}.jpg"
        with open(file_name, 'wb') as file:
            file.write(image_data)
            print(f"✅ Downloaded image: {file_name}")

        count += 1

        driver.close()
        driver.switch_to.window(original_tab)
        time.sleep(random.choice(time_series))

    except NoSuchElementException as e:
        print(f"Element not found: {e}")

    except TimeoutException as e:
        print(f"Timeout occurred while waiting for an element: {e}")

    except StaleElementReferenceException as e:
        print(f"Stale element reference: {e}")

    except ElementNotInteractableException as e:
        print(f"Element not interactable: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        if driver.current_window_handle != original_tab:
            driver.switch_to.window(original_tab)




