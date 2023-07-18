from db_actions import get_base_data
from get_html import save_html_loacl, get_by_css
from vse_instrumenti import vse_instrumenti_get_info
import time

result = get_base_data("SELECT * FROM `product_information` WHERE `marketplace`='ВсеИнструменты.Ру' ORDER BY RAND()")

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
    text_elem = ""
    if item['marketplace'] == "ОЗОН":
        text_elem = get_by_css(item['link'], xpatch_dict['ОЗОН'])
    if item['marketplace'] == "ЯндексМаркет":
        text_elem = get_by_css(item['link'], xpatch_dict['ЯндексМаркет'])
    if item['marketplace'] == "ВсеИнструменты.Ру":
        text_elem = vse_instrumenti_get_info(item['link'], item['width'])

    print(f"Товар: {item['name']}  \nМркетплейс: {item['marketplace']}\nЦена: {text_elem} \n---- \n")
    time.sleep(2)

# lnk = "https://market.yandex.ru/product--shlang-10m-rukav-naporno-vsasyvaiushchii-dlia-drenazhnogo-nasosa-diametr-50-mm-2-morozostokii/1835544502?cpc=FMN1DR1Bua1wilO_mFCzN1CggfHNZAb7YKgs_zBrdy8UadT3f4rSA_HNgEqlbTmeo-irDLkqK50qHi2C2IbMvU6gKmh8sZx-CZ2FI5iAHVVRVF41YHAjrkO_MASBcTKUALpypbsYTgDG9k7DDDK290OoqQ9JWhWakCNYNbL1IgyC6DwMTbY130BCYyhWDoRp28J3-XKuK-dj1zT1Kcm0omI5DWH6EX2o_Cd6Q44cAJVh8kJTjibwDUKm9G3J9_IIdTrYoUbXkeEamfu0-QGhKg%2C%2C&sku=101644629196&do-waremd5=4d6tdxiQZV1nhCZcSzDf4A&sponsored=1&cpa=1&nid=18033952"
# text_elem = get_by_css(lnk, 'h3.fhbmm')
# print(text_elem)