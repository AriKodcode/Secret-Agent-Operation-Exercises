from agent import Agent
from CyberAgent import CyberAgent
from FieldAgent import FieldAgent

agent1 = CyberAgent("ari",1,"iran Nuclear system ")
agent2 = Agent("meir", 11)
agent3 = FieldAgent("moti", 111,"yeman")




def report_agents(list1):
    for agent in list1:
        agent.report()

