import urllib.request
from bs4 import BeautifulSoup


def get_source(url):
    """ Return HTML source of requested url"""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        page_source = response.read()
        return page_source


def get_subcat(site_url):
    """ Return list of urls to all subcategories in the site"""
    selector = ".w25p.pb10 > a"             # CSS Selector for Subcategories in page
    page_source = get_source(site_url)

    # Parse html source DOM
    html_DOM = BeautifulSoup(page_source, "html.parser")
    # Save all href attributes in a list
    subcats = [a.get('href') for a in html_DOM.select(selector)]

    return subcats


def get_subcat_pages(subcat_url):
    """ Return a url list of subcategory product pages divided by pagination """
    page_source = get_source(subcat_url)
    html_DOM = BeautifulSoup(page_source, "html.parser")

    # CSS Selector for pagination buttons in products page
    selector = ".paging-wrapper a.paging.paging-color"
    pages = html_DOM.select(selector)

    # Check if there is no pagination
    if not pages:
        return [subcat_url]

    # Get the last page index in pagination
    last_page_index = int(pages[-1].get_text())

    # Generate URL for paginated products pages
    subcat_pages = ["%spage.%d/" % (subcat_url, i) for i in range(1, last_page_index + 1)]
    return subcat_pages


def get_page_items(page_url):
    """  Return a list of product url"""
    page_source = get_source(page_url)
    if not page_source: return
    html_DOM = BeautifulSoup(page_source, "html.parser")

    # CSS Selectors for Item div, title, price, url
    item_selector = "div.item"
    item_url_selector = "a.item-title-text"
    item_title_selector = "a.item-title-text"
    item_price_selector = "span.item-price"

    # Select all Item divs
    items = html_DOM.select(item_selector)

    # Get Title, Price, and URL of the products
    items_detail = [(item.select(item_title_selector)[0].get_text(),
                     item.select(item_price_selector)[0].get_text(),
                     item.select(item_url_selector)[0].get('href')) for item in items]

    return items_detail

if __name__ == "__main__":

    site_url = "http://meghdadit.com/"

    # print(get_source(site_url))
    # print(get_subcat(site_url))
    # print(get_subcat_pages('http://meghdadit.com/productlist/20/b.19/ipp.40/'))
    print(get_page_items('http://meghdadit.com/productlist/20/b.19/ipp.40/page.1/'))
