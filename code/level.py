from code.entity import Entity

class Level:
    def __init__(self, window, name, mode_option):
        self.window = window
        self.name = name
        self.mode_option = mode_option
        self.entity_list: list[Entity] = []

    def run(self):
        pass
