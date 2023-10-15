from tool import Tool


class SelectionTool(Tool):
    def mouse_down(self):
        print("selection tool selected")

    def mouse_up(self):
        print("select an area")
