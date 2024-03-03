from Configuration import test_metrics, env_metrics


import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
import pickle


class mountaincar:
    
    def __init__(self):
        #Imported Metrics
        self.env_metrics = env_metrics()
        self.test_metrics = test_metrics()
        
        #Class Specific Metrics
        self.pos_space = 0              #Postion
        self.vel_space = 0              #Space
        self.is_training = False        #Training
        
        
    
    
    #Making the Environment 
    def environment(self):
        env = gym.make('MountainCar-v0', render_mode='human' if self.test_metrics.render else None)
        
        return env
    
    
    'Divide position and velocity into segments'
    #Get Position 
    def postion(self,env):
        
        self.pos_spac = np.linspace(env.observation_space.low[0], env.observation_space.high[0], 20)    # Between -1.2 and 0.6
        
    #Get Velocity 
    def velocity(self,env):
        
        self.vel_space = np.linspace(env.observation_space.low[1], env.observation_space.high[1], 20)    # Between -0.07 and 0.07
            