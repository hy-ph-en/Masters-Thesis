import gym
from Testing.Configuration import env_metrics
from Learning.Models.common.env_util import make_vec_env
from Learning.Models.common.monitor import Monitor
from Learning.Models.common.vec_env import SubprocVecEnv

class Environments:
    #List of all possible environments to call upon 
    def __init__(self):
        'Environment Choice'
        self.env = env_metrics().environment
    
    def environmental_choice(self):
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
            9: "CartPole-v1"
        }

        #Making an returning the Environment

        return make_vec_env(env_dict.get(self.env, "CartPole-v1"), n_envs=4, monitor_dir='Logfile')

