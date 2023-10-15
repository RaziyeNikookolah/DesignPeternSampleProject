from convas import Convas
from selection_tool import SelectionTool
from brush_tool import BrushTool

if __name__ == "__main__":
    convas = Convas()
    convas._current_tool = BrushTool()
    convas._current_tool.mouse_down()
    convas._current_tool.mouse_up()
