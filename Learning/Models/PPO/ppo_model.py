from Learning.Models.PPO.ppo import PPO
from Testing.Configuration import env_metrics, test_metrics


def ppo_model(env):
    
    #Metric Imports
    test_metric = test_metrics()
    learning_policy = test_metric.learning_policy
    verbose = test_metric.verbose
    epoches = test_metric.epochs
    
    env = env.environment()
    
    #Model Creation
    model = PPO(learning_policy, env, verbose)
    
    #Model Training
    model.learn(total_timesteps=epoches)
    
    
    
    