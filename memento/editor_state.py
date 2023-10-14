class EditerState:
    def __init__(self, content=None, font_name=None, font_size=None):
        self._content = content
        self._font_name = font_name
        self._font_size = font_size

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        raise AttributeError("Cannot set the content attribute")

    @property
    def font_name(self):
        return self._font_name

    @font_name.setter
    def font_name(self, value):
        self._font_name = value

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def content(self, value):
        self._font_size = value
