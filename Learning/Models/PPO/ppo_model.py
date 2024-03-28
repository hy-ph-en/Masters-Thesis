from Learning.Models.PPO.common.env_util import make_vec_env
from Learning.Models.PPO.ppo import PPO
from Testing.Configuration import env_metrics, test_metrics


def ppo_model(env):
    
    #Metric Imports
    test_metric = test_metrics()
    learning_policy = test_metric.learning_policy
    verbose = test_metric.verbose
    epoches = test_metric.epochs
    
    env = env.environment()
    
    #temepo
    v_env = make_vec_env("CartPole-v1", n_envs=4)
    
    #Model Creation
    model = PPO(learning_policy, v_env, verbose=verbose)
    
    #Model Training
    model.learn(total_timesteps=epoches)
    
    model.save("ppo_cartpole")
    
    del model # remove to demonstrate saving and loading
    
    model = PPO.load("ppo_cartpole")

    obs = v_env.reset()
    while True:
        action, _states = model.predict(obs)
        obs, rewards, dones, info = v_env.step(action)
        v_env.render("human")
    
    
    
    