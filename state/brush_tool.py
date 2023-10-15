from tool import Tool


class BrushTool(Tool):
    def mouse_down(self):
        print("brush tool selected")

    def mouse_up(self):
        print("draw with brush tool")
