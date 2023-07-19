import re
def all_price_clear(price):
    return re.sub("[^0-9]", "", price)