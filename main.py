from db_actions import get_base_data
from myandex_market import yandex_market_get_info
from ozon import ozon_get_info
from vse_instrumenti import vse_instrumenti_get_info
import time
import random

result = get_base_data("SELECT * FROM `product_information` WHERE `marketplace`='ЯндексМаркет' OR `marketplace`='ОЗОН' OR `marketplace`='ВсеИнструменты.Ру' ORDER BY RAND()")

xpatch_dict = {
    'ОЗОН': 'span.qk0',
    'TITAN LOCK': '.price-wrapper .price-wrapper__item:first-child .price_value',
    'ВсеИнструменты.Ру': 'p[data-behavior="price-now"]',
    'Кирелис': '.price-item-card .normal-price',
    'МПТ-Пластик': '',
    'ООО ПК "Хольцер Флексо"': '',
    'Промресурссервис': '.buy .price:first-child .green',
    'Ринком': '.price_matrix_wrapper .price .values_wrapper',
    'Техно-Хаус': '.catalog_item_price',
    'ЯндексМаркет': 'h3.fhbmm',
}

for item in result:
    result = ""
    print(f"Товар: {item['name']}  \nМркетплейс: {item['marketplace']}\n")
    if item['marketplace'] == "ОЗОН":
        result = ozon_get_info(item['link'], item['width'])
    if item['marketplace'] == "ЯндексМаркет":
        result = yandex_market_get_info(item['link'], item['width'])
    if item['marketplace'] == "ВсеИнструменты.Ру":
        result = vse_instrumenti_get_info(item['link'], item['width'])
    print(result)
    print("------")
    time.sleep(random.randint(10, 30))
