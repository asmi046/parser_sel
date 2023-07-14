from db_actions import get_base_data
from save_html import save_html_loacl, get_by_css
import time

result = get_base_data()

xpatch_dict = {
    'ОЗОН': 'span.kr9',
    'TITAN LOCK': '',
    'ВсеИнструменты.Ру': '',
    'Кирелис': '',
    'МПТ-Пластик': '',
    'ООО ПК "Хольцер Флексо"': '',
    'Промресурссервис': '',
    'Ринком': '',
    'Техно-Хаус': '',
    'ЯндексМаркет': 'h1',
}

# for item in result:
#     text_elem = ""
#     if item['marketplace'] == "ОЗОН":
#         text_elem = get_by_css(item['link'], xpatch_dict['ОЗОН'])
#     if item['marketplace'] == "ЯндексМаркет":
#         text_elem = get_by_css(item['link'], xpatch_dict['ЯндексМаркет'])
#
#     print(f"Товар: {item['name']}  \nМркетплейс: {item['marketplace']}\nЦена: {text_elem} \n---- \n")
#     time.sleep(5)

lnk = "https://market.yandex.ru/product--shlang-10m-rukav-naporno-vsasyvaiushchii-dlia-drenazhnogo-nasosa-diametr-50-mm-2-morozostokii/1835544502?cpc=FMN1DR1Bua1wilO_mFCzN1CggfHNZAb7YKgs_zBrdy8UadT3f4rSA_HNgEqlbTmeo-irDLkqK50qHi2C2IbMvU6gKmh8sZx-CZ2FI5iAHVVRVF41YHAjrkO_MASBcTKUALpypbsYTgDG9k7DDDK290OoqQ9JWhWakCNYNbL1IgyC6DwMTbY130BCYyhWDoRp28J3-XKuK-dj1zT1Kcm0omI5DWH6EX2o_Cd6Q44cAJVh8kJTjibwDUKm9G3J9_IIdTrYoUbXkeEamfu0-QGhKg%2C%2C&sku=101644629196&do-waremd5=4d6tdxiQZV1nhCZcSzDf4A&sponsored=1&cpa=1&nid=18033952"
text_elem = get_by_css(lnk, 'h1')

print(text_elem)