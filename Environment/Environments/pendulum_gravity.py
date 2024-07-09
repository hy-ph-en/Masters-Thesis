import gymnasium as gym
import math
import numpy as np
from gymnasium.wrappers import TimeLimit
from gymnasium import spaces
from typing import Optional
from gymnasium.envs.classic_control import PendulumEnv


#Just get it to run and then modify it
class PendulumGravity(PendulumEnv):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(PendulumGravity, self).__init__()

        self.g = 12.5

        #height change
        #gravity change