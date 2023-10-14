class Editor:
    def __init__(self, content):
        self.__content = content

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

    def create_state(self):
        ...

    def restore_state(self):
        ...
