class EditerState:
    def __init__(self, content):
        self.__content = content

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        raise AttributeError("Cannot set the content attribute")
