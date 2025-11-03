from CyberAgent import CyberAgent
from FieldAgent import FieldAgent
from agent import Agent
from mission import Mission
from agent_list import report_agents,agent1,agent2,agent3

if __name__ == "__main__":
    agent = Agent("ari", "66")
    mission = Mission("banana", "gaza", agent)
    mission.brief()
    agent.report()
    agent.get_total_agents()

    agents = [
        agent1,
        agent2,
        agent3,
    ]

    report_agents(agents)



