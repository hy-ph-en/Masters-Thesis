import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
import pickle

from Testing.Configuration import test_metrics, env_metrics


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
    
    
            