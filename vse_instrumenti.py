from get_html import get_by_css
def vse_instrumenti_get_info(url, size=0):
    selector = 'p[data-behavior="price-now"]'
    rez = get_by_css(url, selector)
    return rez