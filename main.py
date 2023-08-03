from db_actions import get_base_data
from get_html import place_get_info
import time
import random

result = get_base_data("SELECT * FROM `product_information` WHERE `marketplace` LIKE '%ЯндексМаркет%' ORDER BY RAND()")

float_price = {
    'ОЗОН': False,
    'TITAN LOCK': False,
    'ВсеИнструменты.Ру': False,
    'Кирелис': False,
    'МПТ-Пластик': False,
    'ООО ПК "Хольцер Флексо"': True,
    'Промресурссервис': True,
    'Ринком': False,
    'Техно-Хаус': True,
    'ЯндексМаркет': False,
}

css_selectors_dict = {
    'ОЗОН': 'div[data-widget="webPrice"] span:first-child',
    'TITAN LOCK': '.price-wrapper .price-wrapper__item:first-child .price_value',
    'ВсеИнструменты.Ру': 'p[data-behavior="price-now"]',
    'Кирелис': '.price-item-card .normal-price',
    'МПТ-Пластик': '.price_new span.price_val',
    'ООО ПК "Хольцер Флексо"': 'span.product-detail-price-current',
    'Промресурссервис': '.buy .price:first-child .green',
    'Ринком': '.price_matrix_wrapper .price .values_wrapper',
    'Техно-Хаус': '.catalog-items.offers .catalog_item_price',
    'ЯндексМаркет': 'h3.fhbmm',
}

for item in result:
    result = ""
    print(f"Товар: {item['name']}  \nМркетплейс: {item['marketplace']}\n")
    result = place_get_info(item['link'], item['width'], css_selectors_dict[item['marketplace']], float_price[item['marketplace']])

    print(result)
    print("------")
    time.sleep(random.randint(10, 30))
