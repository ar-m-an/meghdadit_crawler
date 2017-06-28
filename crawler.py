import urllib.request


def get_source(url):
    """ Return HTML source of requested url"""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        page_source = response.read()
        return page_source


def get_subcat(site_url):
    """ Return list of urls to all subcategories in the site"""


def get_subcat_pages(subcat_url):
    """ Return a url list of subcategory product pages divided by pagination """


def get_page_items(page_url):
    """  Return a list of product url"""


if __name__ == "__main__":

    site_url = "http://meghdadit.com/"

    print(get_source(site_url))
