import random

from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
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

def get_by_css(page, query):
    browser = webdriver.Chrome()
    browser.get(page)
    browser.implicitly_wait(random.randint(10,30))
    try:
        return browser.find_element(By.CSS_SELECTOR, query).text
    except Exception as ex:
        return "Ненайдено..."