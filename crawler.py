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


def get_page_items(page_url):
    """  Return a list of product url"""


if __name__ == "__main__":

    site_url = "http://meghdadit.com/"

    # print(get_source(site_url))
    print(get_subcat(site_url))
