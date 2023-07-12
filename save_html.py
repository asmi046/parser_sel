from selenium import webdriver
from datetime import datetime
import codecs
import os
def save_html_loacl(page, id):
    time = datetime.now()
    filename = f"{id}_{time.day}-{time.month}-{time.year}.html"
    dir = "html"

    browser = webdriver.Chrome()
    browser.get( page )
    html = browser.page_source

    if not os.path.exists(dir):
        os.mkdir(dir)

    file = codecs.open(f"{dir}//{filename}", "w", "utf-8")
    file.write( html )
    file.close()

    return filename
