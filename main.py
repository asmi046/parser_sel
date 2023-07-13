from db_actions import get_base_data
from save_html import save_html_loacl

result = get_base_data()

for item in result:
    new_fn = save_html_loacl(item['link'], item['id'])
    print(f"Страница: {item['link']} сохранена в: {new_fn}")
