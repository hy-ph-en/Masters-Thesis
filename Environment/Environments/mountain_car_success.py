import gymnasium as gym
import math
import numpy as np
from gymnasium.wrappers import TimeLimit
from gymnasium import spaces
from typing import Optional
from gymnasium.envs.classic_control import MountainCarEnv


#Just get it to run and then modify it
class MountainCarSuccess(MountainCarEnv):

    def __init__(self, goal_velocity=0, render_mode="human"):
        super().__init__()
        self.goal_velocity = goal_velocity
        self.render_mode = render_mode

    def step(self, action: int):
        assert self.action_space.contains(
            action
        ), f"{action!r} ({type(action)}) invalid"

        position, velocity = self.state
        velocity += (action - 1) * self.force + math.cos(3 * position) * (-self.gravity)
        velocity = np.clip(velocity, -self.max_speed, self.max_speed)
        position += velocity
        position = np.clip(position, self.min_position, self.max_position)
        if position == self.min_position and velocity < 0:
            velocity = 0

        terminated = bool(
            position >= self.goal_position      #removed goal speed, just position should matter
        )
        reward = -1.0

        self.state = (position, velocity)
        if self.render_mode == "human":
            self.render()
        # truncation=False as the time limit is handled by the `TimeLimit` wrapper added during `make`
        return np.array(self.state, dtype=np.float32), reward, terminated, False, {}
    
    def render(self):
        if self.render_mode not in ['human', 'rgb_array']:
            raise ValueError("Invalid render mode. Must be 'human' or 'rgb_array'.")
        print("dooooo")
        return super().render(mode=self.render_mode)  # Call the superclass render method


