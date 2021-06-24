import random

class Object:
    def __repr__(self):
        return '<%s>' % getattr(self,'__name__',self.__class__.__name__)


class Agent(Object):
    def __init__(self):
        def program(percept):abstract
        self.program=program

loc_A, loc_B, loc_C, loc_D = 'A', 'B', 'C', 'D'

class vaccumEnvironment():
    def __init__(self):
        self.status = { loc_A:random.choice(['Clean','Dirty']),
                      loc_B:random.choice(['Clean','Dirty']),
                      loc_C:random.choice(['Clean','Dirty']),
                      loc_D:random.choice(['Clean','Dirty']),
                      }
    def add_object(self,object,location=None):
        object.location = location or self.default_location(object)

    def default_location(self,object):
        return random.choice([loc_A,loc_B,loc_C,loc_D])

    def percept(self,agent):
        return (agent.location,self.status[agent.location])

    def execute_action(self,agent,action):
        if action == 'Right': agent.location = random.choice([loc_B,loc_D])
        elif action == 'Down': agent.location = random.choice([loc_C,loc_D])
        elif action == 'Left': agent.location = random.choice([loc_A,loc_C])
        elif action == 'Up': agent.location = random.choice([loc_A,loc_B])
        elif action == 'Suck': self.status[agent.location] = 'Clean'

class modelBasedVaccumAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        model = {loc_A:None,loc_B:None,loc_C:None,loc_D:None}

        def program(percept):
            location = percept[0]
            status = percept[1]

            model[location] = status
            if model[loc_A] == model[loc_B] == model[loc_C] == model[loc_D] == 'Clean': return 'NoOp'
            if status == 'Dirty': action = 'Suck'
            elif location == loc_A: action = random.choice(['Right','Down'])
            elif location == loc_B: action = random.choice(['Left','Down'])
            elif location == loc_C: action = random.choice(['Up','Right'])
            elif location == loc_D: action = random.choice(['Up','Left'])

            percept=(location,status)
            print('Agent perceives ', percept, ' and does ', action)

            return action                    

        self.program = program

MBAgent = modelBasedVaccumAgent()
VacEnv = vaccumEnvironment()
VacEnv.add_object(MBAgent)
for _ in range(15):
    action = MBAgent.program(VacEnv.percept(MBAgent))
    VacEnv.execute_action(MBAgent,action)
