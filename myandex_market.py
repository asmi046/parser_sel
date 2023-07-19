from time import sleep
from get_html import get_by_css
import random

from price_clear import all_price_clear


def yandex_market_get_info(url, size=0):
    selector = 'h3.fhbmm'
    print(f'Начинаем разбор...')
    rez = get_by_css(url, selector)
    print(rez)

    if rez == False:
        sec = random.randint(10,30)
        print(f'Попытка не удалась повторим через {sec}')
        sleep(sec)

        rez = get_by_css(url, selector)
        if rez == False:
            print(f'Опять косяк надо еще что то придумать...')

    if rez != False:
        rez_cer = float(all_price_clear(rez))
        rez_cer_metr = rez_cer / size

        return {'src': rez, 'rez_cer': rez_cer, 'metr':rez_cer_metr}
    else:
        return rez