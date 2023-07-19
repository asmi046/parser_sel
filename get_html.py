import random
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from config import CHROME_PROFILE_DIR, CHROME_USER_DATA_DIR
from fake_useragent import UserAgent
import codecs
import os


def save_html_loacl(page, id):
    time = datetime.now()
    filename = f"{id}_{time.day}-{time.month}-{time.year}.html"
    dir = "html"

    browser = webdriver.Chrome()
    browser.get(page)
    html = browser.page_source

    if not os.path.exists(dir):
        os.mkdir(dir)

    file = codecs.open(f"{dir}//{filename}", "w", "utf-8")
    file.write(html)
    file.close()

    return filename


def get_by_xpatch(page, patch):
    browser = webdriver.Chrome()
    browser.get(page)
    browser.implicitly_wait(5)
    try:
        return browser.find_element(By.XPATH, patch).text
    except Exception as ex:
        return "Ненайдено..."

def get_by_css(page, query, proxy=""):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'profile-directory={CHROME_PROFILE_DIR}')
    chrome_options.add_argument(f"user-data-dir={CHROME_USER_DATA_DIR}")

    ua = UserAgent(browsers=["chrome", "edge", "firefox", "opera"])
    chrome_options.add_argument(f"--user-agent={ua.random}")

    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    if proxy != "":
        chrome_options.add_argument(f"--proxy-server=={proxy}")

    browser = webdriver.Chrome(options=chrome_options)

    browser.get(page)
    browser.implicitly_wait(random.randint(10,50))
    try:
        return browser.find_element(By.CSS_SELECTOR, query).text
    except Exception as ex:
        return False
    finally:
        browser.close()
        browser.quit()