from Testing.Configuration import env_metrics

from Environment.Environments.mountain_car import mountaincar
#from noisy_road import 


class Environments:
    #List of all possible environments to call upon 
    def __init__(self):
        'Environment Choice'
        self.env = env_metrics().environment
        
        'Environments'
        self.mountaincar = mountaincar()
        self.noisyroad2d = 0 #noisyroad2d()
        self.noisyroad = 0 #noisyroad()
        self.obstacle = 0 #obstacle()
        self.obstacle2 = 0 #obstacle2()
        self.pendulum = 0 #pendulum()
        self.road2d = 0 #road2d()
        self.road = 0 #road()
    
    
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
    