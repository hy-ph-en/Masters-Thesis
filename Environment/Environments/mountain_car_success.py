import gymnasium as gym
import math
import numpy as np
from gymnasium.wrappers import TimeLimit
from gymnasium import spaces
from typing import Optional
from gymnasium.envs.classic_control import MountainCarEnv


#Just get it to run and then modify it
class MountainCarSuccess(MountainCarEnv):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(MountainCarSuccess, self).__init__()

        #speed change?

        #the training is on normal mountain car and the testing is on continous mountain car, then you can compare the outputs