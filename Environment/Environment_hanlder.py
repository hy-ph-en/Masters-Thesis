from mountain_car import mountaincar
from Configuration import env_metrics 
#from noisy_road import 


class Environments:
    #List of all possible environments to call upon 
    def __init__(self):
        'Environment Choice'
        self.env = env_metrics.environment
        
        'Environments'
        self.mountaincar = mountaincar()
        self.noisyroad2d = noisyroad2d()
        self.noisyroad = noisyroad()
        self.obstacle = obstacle()
        self.obstacle2 = obstacle2()
        self.pendulum = pendulum()
        self.road2d = road2d()
        self.road = road()
    
    
    def environmental_choice(self):
        #List of environments
        env_dict = {
            1: self.mountaincar, 
            2: self.noisyroad2d,
            3: self.noisyroad,
            4: self.obstacle,
            5: self.obstacle2,
            6: self.pendulum,
            7: self.road2d,
            8: self.road
        }
        
        #If improper input, default to mountain car environment
        return env_dict.get(self.env, self.mountaincar)
        