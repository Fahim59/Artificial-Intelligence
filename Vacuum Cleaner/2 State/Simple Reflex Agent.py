import random

class Object:
    def __repr__(self):
        return '<%s>' % getattr(self,'__name__',self.__class__.__name__)


class Agent(Object):
    def __init__(self):
        def program(percept):abstract
        self.program=program

loc_A, loc_B = 'A', 'B'

class vaccumEnvironment():
    def __init__(self):
        self.status = { loc_A:random.choice(['Clean','Dirty']),
                      loc_B:random.choice(['Clean','Dirty'])
                      }
    def add_object(self,object,location=None):
        object.location = location or self.default_location(object)

    def default_location(self,object):
        return random.choice([loc_A,loc_B])

    def percept(self,agent):
        return (agent.location,self.status[agent.location])

    def execute_action(self,agent,action):
        if action == 'Right': agent.location = loc_B
        elif action == 'Left': agent.location = loc_A
        elif action == 'Suck': self.status[agent.location] = 'Clean'

class reflexVaccumAgent(Agent):

    def __init__(self):
        Agent.__init__(self)        

        def program(percept):
            location = percept[0]
            status = percept[1]
            if status == 'Dirty': action= 'Suck'
            elif location == loc_A: action= 'Right'
            elif location == loc_B: action= 'Left'

            percept=(location,status)
            print('Agent perceives ', percept, ' and does ', action)

            return action

        self.program = program

RBAgent = reflexVaccumAgent()
VacEnv = vaccumEnvironment()
VacEnv.add_object(RBAgent)
for _ in range(15):
    action = RBAgent.program(VacEnv.percept(RBAgent))
    VacEnv.execute_action(RBAgent,action)
