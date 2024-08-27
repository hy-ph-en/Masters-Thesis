import gymnasium as gym
import math
import numpy as np
from gymnasium.wrappers import TimeLimit
from gymnasium import spaces
from typing import Optional
from gymnasium.envs.classic_control import MountainCarEnv


#Just get it to run and then modify it
class MountainCarSpeed(MountainCarEnv):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(MountainCarSpeed, self).__init__()

        self.max_speed = 0.075
        


        #speed change?
        #An even lower speed could cause issues with solving the problem