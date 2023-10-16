from iterator import Iterator


class BrowserIterator(Iterator):
    def __init__(self, urls):
        self.urls = urls
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.urls):
            value = self.urls[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration
