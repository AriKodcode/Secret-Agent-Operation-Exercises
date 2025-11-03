from agent import Agent

class CyberAgent(Agent):
    def __init__(self,code_name, clearance_level, hacking):
        super().__init__(code_name, clearance_level)
        self.hacking = hacking

    def report(self):
        print(f"Agent {self.code_name}, reporting {self._clearance_level}, hacking: {self.hacking}")