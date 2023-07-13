from db_actions import get_base_data
from save_html import save_html_loacl, get_by_xpatch
import time

result = get_base_data()

for item in result:
    if item['marketplace'] == "ОЗОН":
        text_elem = get_by_xpatch(item['link'], '/html/body/div[1]/div/div[1]/div[4]/div[3]/div[3]/div/div[14]/div/div[1]/div/div/div[1]/div[2]/div/div[1]/span[1]')
        #new_fn = save_html_loacl(item['link'], item['id'])
        #print(f"Страница: {item['link']} сохранена в: {new_fn}")
        print(f"Результат: {text_elem} ")
        time.sleep(5)


"""
TITAN LOCK
ВсеИнструменты.Ру
Кирелис
МПТ-Пластик
ОЗОН
ООО ПК "Хольцер Флексо"
Промресурссервис
Ринком
Техно-Хаус
ЯндексМаркет
"""