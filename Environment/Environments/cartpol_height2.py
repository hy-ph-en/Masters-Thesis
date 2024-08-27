import gymnasium as gym
import math
import numpy as np
from gymnasium.wrappers import TimeLimit
from gymnasium import spaces
from typing import Optional
from gymnasium.envs.classic_control import CartPoleEnv


#Just get it to run and then modify it
class CartPoleHeight2(CartPoleEnv):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(CartPoleHeight2, self).__init__()

        self.length = 1

        #height change
        #gravity change