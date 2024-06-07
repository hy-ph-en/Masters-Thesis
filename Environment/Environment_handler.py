import gym
import gymnasium
from Testing.Configuration import env_metrics
from Learning.Models.common.env_util import make_vec_env
from Environment.Environments.mountain_car_success import MountainCarSuccess

class Environments:
    #List of all possible environments to call upon 
    def __init__(self):
        'Environment Choice'
        self.env = env_metrics().environment
    
    def environmental_choice(self, custom_run=False):
        #Load Registered Environments
        self.registration()

        #List of environments
        env_dict = {
            1: "MountainCar-v0", 
            2: "noisy_road_2d",
            3: "noisy_road",
            4: "obstacle",
            5: "obstacle2",
            6: "Pendulum-v1",
            7: "road_2d",
            8: "road",
            9: "CartPole-v1",
            10:"MountainCarSuccess-v0",
            11:"PendulumLength-v0",
        }

        #If it is required the rerun the model over a novel environment
        if custom_run == True:
            self.env = env_metrics().custom_environment_test

        #Making an returning the Environment
        return make_vec_env(env_dict.get(self.env, "CartPole-v1"), n_envs=4, monitor_dir='Logfile')

    def registration(self):
        from gymnasium.envs.registration import register

        #Custom Mountain Car-v0
        register(
            id='MountainCarSuccess-v0',
            entry_point='Environment.Environments.mountain_car_success:MountainCarSuccess',  # Update this to the path where the CustomCartPoleEnv class is located
            max_episode_steps=200,
        )

        #Custom Pendulum - Length Change
        register(
            id='PendulumLength-v0',
            entry_point='Environment.Environments.pendulum_height:PendulumHeight',
            max_episode_steps=200,
        )