import random
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from config import CHROME_PROFILE_DIR, CHROME_USER_DATA_DIR
from fake_useragent import UserAgent
import codecs
import os
from time import sleep

from get_proxy import get_valid_proxy
from price_clear import all_price_clear


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

def get_by_css(page, query, proxy = "", headless = False):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'profile-directory={CHROME_PROFILE_DIR}')
    chrome_options.add_argument(f"user-data-dir={CHROME_USER_DATA_DIR}")

    ua = UserAgent(browsers=["chrome", "edge", "firefox", "opera"])
    chrome_options.add_argument(f"--user-agent={ua.random}")

    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    if headless:
        chrome_options.add_argument('--headless')

    if proxy != "":
        chrome_options.add_argument(f"--proxy-server=={proxy}")

    browser = webdriver.Chrome(options=chrome_options)


    try:
        browser.get(page)
        browser.implicitly_wait(20)
        element = browser.find_element(By.CSS_SELECTOR, query).text
        return element
    except Exception as ex:
        return False
    finally:
        browser.close()
        browser.quit()

def place_get_info(url, size=0, selector="", floatprice=False):
    headless_mode = True
    if selector == False:
        return False

    print(f'Начинаем разбор...')
    rez = get_by_css(url, selector, headless=headless_mode)
    print(rez)

    if rez == False:
        sec = random.randint(5,10)
        print(f'Попытка не удалась повторим через {sec}')
        sleep(sec)

        rez = get_by_css(url, selector, headless=headless_mode)
        if rez == False:
            print("Пробуем с прокси....")
            proxy_result = get_valid_proxy()
            if proxy_result['status']:
                rez = get_by_css(url, selector, proxy_result['proxy'], headless=headless_mode)

            if rez == False:
                print(f'Опять косяк надо еще что то придумать...')

    if rez != False:
        rez_cer = float(all_price_clear(rez))
        rez_cer_metr = rez_cer / size

        if floatprice:
            rez_cer /= 100
            rez_cer_metr /= 100

        return {'src': rez, 'rez_cer': rez_cer, 'metr':rez_cer_metr}
    else:
        return rez