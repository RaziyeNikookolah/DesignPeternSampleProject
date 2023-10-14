from editor_state import EditerState


class History:
    def __init__(self):
        self.states: list[EditerState] = []

    def push(self, state):
        self.states.append(state)

    def pop(self):
        last_index = len(self.states)
        last_state = self.states[last_index-1]
        self.states.remove(last_state)
        return last_state
