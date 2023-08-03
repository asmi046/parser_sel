from db_actions import get_base_data, create_load_field, update_load_field, create_price_line
from get_html import place_get_info
import time
import random


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
            print(result)
        else:
            bug+=1
            bug_str += f"{item['id']}|{item['name']}|{item['marketplace']}"
            print("ERROR: Не удалось распознать")
            result = {'src': '', 'rez_cer': 0, 'metr': 0}

        print("------")

        create_price_line(price_info=result, tovar_info={'name':item['name'], 'marketplace':item['marketplace']}, load_id=load_id, product_id=item['id'],loadet=result != False)
        time.sleep(random.randint(5, 15))

    update_load_field(id=load_id, count_fine=fine, count_bug=bug, bug_track=bug_str)

if __name__ == "__main__":
    main()
