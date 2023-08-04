from db_actions import get_base_data, create_load_field, update_load_field, create_price_line
from get_html import place_get_info, get_by_css
import time
import random

from get_proxy import get_valid_proxy


def main():
    # result = get_base_data("SELECT * FROM `product_information` WHERE `marketplace` = 'ВсеИнструменты.Ру' ORDER BY RAND()")
    result = get_base_data("SELECT * FROM `product_information` ORDER BY RAND()")

    float_price = {
        'ОЗОН': False,
        'TITAN LOCK': False,
        'ВсеИнструменты.Ру': False,
        'Кирелис': True,
        'МПТ-Пластик': False,
        'ООО ПК "Хольцер Флексо"': True,
        'Промресурссервис': True,
        'Ринком': False,
        'Техно-Хаус': False,
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
    load_id = create_load_field(len(result))
    print(f"Проверка № {load_id}")

    fine = 0
    bug = 0
    bug_str = ""

    for item in result:
        result = ""
        print(f"Товар: {item['name']}  \nМркетплейс: {item['marketplace']}\n")
        result = place_get_info(item['link'], item['width'], css_selectors_dict[item['marketplace']], float_price[item['marketplace']])

        if result != False :
            fine+=1
            loadet_flag = True
            print(result)
        else:
            bug+=1
            bug_str += f"{item['id']}|{item['name']}|{item['marketplace']}"
            loadet_flag = False
            print("ERROR: Не удалось распознать")
            result = {'src': '', 'rez_cer': 0, 'metr': 0}

        print("------")

        create_price_line(price_info=result, tovar_info={'name':item['name'], 'marketplace':item['marketplace']}, load_id=load_id, product_id=item['id'],loadet=loadet_flag)

    update_load_field(id=load_id, count_fine=fine, count_bug=bug, bug_track=bug_str)

def mp_test():
    ozon = [
        'https://www.ozon.ru/product/shlang-10m-rukav-naporno-vsasyvayushchiy-dlya-drenazhnogo-nasosa-diametr-50-mm-2-morozostokiy-504141118/?asb=KRtDMCLLhzS54IuCmpulc%252B5OI4H23MPpTqp1%252B3DcOABqT6T1W02eYM4goCEy2n7U&asb2=ibh_JLK-I2ZFE7Br5mQMHYWkVUy91PKIuf3muFj9wioe1V2G8P4HKR_mnpW_IwYW9XFveIh6mWR46l7HoYws4d_O7KmlWmObHprXLYtq9ZeDCai9mZduPvUYUxYJQHbaxXNYH60csVpNi_qIRQsf3A&avtc=1&avte=2&avts=1684415924&from_sku=504141423&from_url=https%253A%252F%252Fwww.ozon.ru%252Fcategory%252Fshlangi-i-komplekty-dlya-poliva-14641%252F%253Fgardenwateringmaterial%253D30040%25252C27166%2526hosediameter%253D267412%25252C267411%25252C267413%25252C267415%2526hosetype%253D155847%25252C175848%2526tf_state%253DdYly-_JjeaR0_a3tRKnWzsErHYfVfInSgPXuWZ91D8wDVdk%25253D&oos_search=false&sh=wqyUGr55XQ',
        'https://www.ozon.ru/product/shlang-assenizatorskiy-naporno-vsasyvayushchiy-morozostoykiy-d-50mm-dlina-10-metrov-rubex-733592800/?asb=AO4ygTK59rVmLF8KonrtdOt8pfzEsMUQ75OVioUqxUE%253D&asb2=EaTQh3vUd7W5CRSlx3wgRA-3losZnfnksSo9_P9rcDVQE2H7NDdHJps6eRQbeShS&avtc=1&avte=2&avts=1684415924&from_sku=732607396&from_url=https%253A%252F%252Fwww.ozon.ru%252Fcategory%252Fshlangi-i-komplekty-dlya-poliva-14641%252F%253Fgardenwateringmaterial%253D30040%25252C27166%2526hosediameter%253D267412%25252C267411%25252C267413%25252C267415%2526hosetype%253D155847%25252C175848%2526tf_state%253DdYly-_JjeaR0_a3tRKnWzsErHYfVfInSgPXuWZ91D8wDVdk%25253D&oos_search=false&sh=wqyUGnaRWw',
        'https://www.ozon.ru/product/shlang-naporno-vsasyvayushchiy-assenizatorskiy-morozostoykiy-d-50mm-dlina-25-metrov-rubex-736709500/?asb=AO4ygTK59rVmLF8KonrtdOt8pfzEsMUQ75OVioUqxUE%253D&asb2=EaTQh3vUd7W5CRSlx3wgRA-3losZnfnksSo9_P9rcDVQE2H7NDdHJps6eRQbeShS&avtc=1&avte=2&avts=1684415924&from_sku=732607396&from_url=https%253A%252F%252Fwww.ozon.ru%252Fcategory%252Fshlangi-i-komplekty-dlya-poliva-14641%252F%253Fgardenwateringmaterial%253D30040%25252C27166%2526hosediameter%253D267412%25252C267411%25252C267413%25252C267415%2526hosetype%253D155847%25252C175848%2526tf_state%253DdYly-_JjeaR0_a3tRKnWzsErHYfVfInSgPXuWZ91D8wDVdk%25253D&oos_search=false&sh=wqyUGnaRWw',
        'https://www.ozon.ru/product/shlang-dlya-drenazhnogo-nasosa-morozostoykiy-zimniy-morozoustoychivyy-armirovannyy-prozrachnyy-730786242/?asb=eSNYla%252BFt72irygAArptg9MtNsE3GRNbng5gKD%252BwcgQ%253D&asb2=gN3d4-vqgwLkTvFqj8xGtghaZpxI6liv_HD8djNIo0xUQidLdZS0v3-ZHiB4ouON&avtc=1&avte=2&avts=1684417252&from_sku=730786949&from_url=https%253A%252F%252Fwww.ozon.ru%252Fcategory%252Fshlangi-i-komplekty-dlya-poliva-14641%252F%253Fgardenwateringmaterial%253D30040%2526hosediameter%253D267411%2526hosetype%253D155847%25252C175848&oos_search=false&sh=wqyUGmmTSA',
        'https://market.yandex.ru/product--shlang-naporno-vsasyvaiushchii-pvkh-tip-4-75-mm-spiralnyi-morozostoikii-10-metrov/1776262312?cpc=3Xiw91egKI7JGZdjV80M6tRHUVLrMtCi7UTHblH9Ks8C0cgjtjS3hxguGLp9NoGr24PoZZJKGHsAgsYO_UbcTXs_hLBm1U0QXMP83pLqYSBi34LutoSBHkStNL8a6afMl9SVFRDk_utF0zhrf4CmDiTcyu4TEkIWo5piV82KbuFHWYWHKpoIcidNn8cY2zOyUuaHjmHV61w%2C&sku=101847053955&do-waremd5=03Qn81Ve5SmH1VP4Nwmx7w&cpa=1&nid=18033952',
        'https://market.yandex.ru/product--shlang-naporno-vsasyvaiushchii-100-mm-kh-8-m-fht-fubag-838704/101965126879?cpc=5ymvmfBtNJQEcDxhB2I9Vqe4Qp-ksGdujtPTh1iCTUIQ4AFP-z9M8XZYJmKF4aqjCOSqzTAU5-PgWCoEGefDhhbI9QIrQsnGWqfw0a5o2nH4_X-ZCct_gTGebZdEQNhrfPhBcCRWQo1Q1zUcKL36cIBcEE-Z_hWbrZVQxJ6KrB6GBVMyDSKmn21oieRTiZmJYKVrd3vJa0o%2C&sku=101965126879&do-waremd5=l7nlVLtfH_K7Ah3ICxcG8w&cpa=1&nid=18033952',
        'https://market.yandex.ru/product--shlang-10m-rukav-naporno-vsasyvaiushchii-dlia-drenazhnogo-nasosa-diametr-50-mm-2-morozostokii/1835544502?cpc=FMN1DR1Bua1wilO_mFCzN1CggfHNZAb7YKgs_zBrdy8UadT3f4rSA_HNgEqlbTmeo-irDLkqK50qHi2C2IbMvU6gKmh8sZx-CZ2FI5iAHVVRVF41YHAjrkO_MASBcTKUALpypbsYTgDG9k7DDDK290OoqQ9JWhWakCNYNbL1IgyC6DwMTbY130BCYyhWDoRp28J3-XKuK-dj1zT1Kcm0omI5DWH6EX2o_Cd6Q44cAJVh8kJTjibwDUKm9G3J9_IIdTrYoUbXkeEamfu0-QGhKg%2C%2C&sku=101644629196&do-waremd5=4d6tdxiQZV1nhCZcSzDf4A&sponsored=1&cpa=1&nid=18033952',
        'https://market.yandex.ru/product--shlang-naporno-vsasyvaiushchii-pvkh-tip-4-75-mm-spiralnyi-morozostoikii-10-metrov/1776262312?cpc=3Xiw91egKI7JGZdjV80M6tRHUVLrMtCi7UTHblH9Ks8C0cgjtjS3hxguGLp9NoGr24PoZZJKGHsAgsYO_UbcTXs_hLBm1U0QXMP83pLqYSBi34LutoSBHkStNL8a6afMl9SVFRDk_utF0zhrf4CmDiTcyu4TEkIWo5piV82KbuFHWYWHKpoIcidNn8cY2zOyUuaHjmHV61w%2C&sku=101847053955&do-waremd5=03Qn81Ve5SmH1VP4Nwmx7w&cpa=1&nid=18033952',
    ]
    proxy_result = get_valid_proxy()
    proxy = proxy_result['proxy']

    print(proxy)
    rez = get_by_css(page=ozon[5], proxy=proxy, query='h3.fhbmm', headless=False)

    print(rez)

if __name__ == "__main__":
    mp_test()
    # main()
