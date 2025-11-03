from agent import Agent
from mission import Mission
if __name__ == "__main__":
    agent = Agent("ari", "66")
    mission = Mission("banana", "gaza", agent)
    mission.brief()
    agent.set_clearance_level(11)
    print(agent.report())
