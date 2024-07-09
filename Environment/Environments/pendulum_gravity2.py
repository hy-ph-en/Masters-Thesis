import gymnasium as gym
import math
import numpy as np
from gymnasium.wrappers import TimeLimit
from gymnasium import spaces
from typing import Optional
from gymnasium.envs.classic_control import PendulumEnv


#Just get it to run and then modify it
class PendulumGravity2(PendulumEnv):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(PendulumGravity2, self).__init__()

        self.g = 15

        #height change
        #gravity change