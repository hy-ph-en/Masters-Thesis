from Learning.Models.common.env_util import make_vec_env
from Learning.Models.PPO.ppo import PPO
from Testing.Configuration import env_metrics, test_metrics
from Learning.Models.common.logger import configure
import torch

from Environment.Environments.mountain_car_success import MountainCarSuccess


def ppo_model(env):
    
    #Metric Imports
    test_metric = test_metrics()
    learning_policy = test_metric.learning_policy
    verbose = test_metric.verbose
    epoches = test_metric.epochs
    learning_rate = test_metric.ppo_learning_rate
    gamma = test_metric.gamma
    batch_size = test_metric.batch_size
    
    steps = env_metrics().number_of_steps

    #GPU Acceleration
    print(torch.cuda.is_available()) 
    print(torch.version.cuda)
    print("Is CUDA available: ", torch.cuda.is_available())
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    #Model Creation
    model = PPO(learning_policy, env, verbose=verbose, learning_rate=learning_rate, n_epochs=epoches, gamma=gamma, batch_size= batch_size, device=device)

    #Logging Progress
    tmp_path = "Logfile/Baseline_Output"

    new_logger = configure(tmp_path, ["stdout","csv"])

    model.set_logger(new_logger)
    
    #Model Training
    model.learn(total_timesteps=steps)
    
    model.save("Environment_Solution")
    
    del model # remove to demonstrate saving and loading
    
    model = PPO.load("Environment_Solution")

    obs = env.reset()
    while True:
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)
        env.render("human")
    
    
    
    