from url_collection import UrlCollection


if __name__ == "__main__":
    urls = UrlCollection()
    urls.add_url("www.google.com")
    urls.add_url("www.ketab.com")
    urls.add_url("www.sport.com")

    browser_iterator = urls.create_iterator()

    for url in browser_iterator:
        print(url)
