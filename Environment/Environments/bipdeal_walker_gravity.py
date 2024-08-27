import gymnasium as gym
import math
import numpy as np
from gymnasium.wrappers import TimeLimit
from gymnasium import spaces
from typing import Optional
from gymnasium.envs.box2d.bipedal_walker import BipedalWalker


#Just get it to run and then modify it
class BipedalWalkerGravity(BipedalWalker):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(BipedalWalkerGravity, self).__init__()

        self.gravity = 11.25

        #height change
        #gravity change