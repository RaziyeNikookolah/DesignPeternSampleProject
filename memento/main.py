from editor import Editor
from history import History


if __name__ == "__main__":
    editer = Editor()
    history = History()

    editer._content = "salam"
    editer._font_name = "arial"
    editer._font_size = 16

    ed_st = editer.create_state()
    history.push(ed_st)

    editer._content = "hale shoma?"
    editer._font_name = "B-nazanin"
    editer._font_size = 14

    ed_st = editer.create_state()
    history.push(ed_st)

    editer._content = "vaght bekheir"  # here we dont save state and did not push
    editer._font_name = "iran-nastaligh"

    editer.restore_state(history.pop())
    print(editer)
    editer.restore_state(history.pop())
    print(editer)
