from editor_state import EditerState


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
        editer_state = EditerState(self.__content)
        return editer_state

    def restore_state(self, editer_state):
        self.__content = editer_state
