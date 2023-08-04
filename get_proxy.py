import requests
from fp.fp import FreeProxy


def check_proxy(px):
    try:
        requests.get("https://www.google.com/", proxies = {"https": px}, timeout = 2)
    except Exception as x:
        return False
    return True

def get_valid_proxy():
    valid_proxy_flag = False
    proxy = ""
    i = 0
    while not valid_proxy_flag:
        try:
            proxy = FreeProxy(country_id=['RU'], https=True, anonym=True).get()
            valid_proxy_flag = check_proxy(proxy)
        except:
            valid_proxy_flag = False
        i+=1
        if i > 10: break


    return {'proxy':proxy, 'status':valid_proxy_flag, 'iteration': i}