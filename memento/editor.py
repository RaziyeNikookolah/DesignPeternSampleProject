from editor_state import EditerState


class Editor:
    def __init__(self, content=None, font_name=None, font_size=None):
        self._content = content
        self._font_name = font_name
        self._font_size = font_size

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

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
    def font_size(self, value):
        self._font_size = value

    def create_state(self):
        editer_state = EditerState(
            self._content, self._font_name, self._font_size)
        return editer_state

    def restore_state(self, editer_state):
        self._content = editer_state._content
        self._font_name = editer_state._font_name
        self._font_size = editer_state._font_size

    def __str__(self):
        return f"Contect:{self._content:12}  Font name:{self._font_name:12}  Font size:{self._font_size:12}"
