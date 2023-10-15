from tool import Tool


class Convas:
    def __init__(self) -> None:
        self._current_tool: Tool = None

    @property
    def current_tool(self):
        return self._current_tool

    @current_tool.setter
    def current_tool(self, value):
        self._current_tool = value

    def mouse_down(self):
        self._current_tool.mouse_down()

    def mouse_up(self):
        self._current_tool.mouse_up()
