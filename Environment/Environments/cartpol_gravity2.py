import gymnasium as gym
import math
import numpy as np
from gymnasium.wrappers import TimeLimit
from gymnasium import spaces
from typing import Optional
from gymnasium.envs.classic_control import CartPoleEnv


#Just get it to run and then modify it
class CartPoleGravity2(CartPoleEnv):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(CartPoleGravity2, self).__init__()

        self.gravity = 15

        #height change
        #mass change?