from browser_iterator import BrowserIterator


class UrlCollection:
    def __init__(self):
        self.urls = []

    def add_url(self, url):
        self.urls.append(url)

    def create_iterator(self):
        return BrowserIterator(self.urls)
