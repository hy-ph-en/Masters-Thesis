import gymnasium as gym
import math
import numpy as np
from gymnasium.wrappers import TimeLimit
from gymnasium import spaces
from typing import Optional
from gymnasium.envs.classic_control import CartPoleEnv


#Just get it to run and then modify it
class CartPoleGravity(CartPoleEnv):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(CartPoleGravity, self).__init__()

        self.gravity = 12.5

        #height change
        #mass change?