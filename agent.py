class Agent:

    def __init__(self, code_name, clearance_level):
        self.code_name = code_name
        self._clearance_level = clearance_level

    def report(self):
        print(f"Agent {self.code_name}, reporting {self._clearance_level}")

    def get_clearance_level(self):
        return self._clearance_level

    def set_clearance_level(self, level):
        if 1 < level < 10:
            self._clearance_level = level
            return level
