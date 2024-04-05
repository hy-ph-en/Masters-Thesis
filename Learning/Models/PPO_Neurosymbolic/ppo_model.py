from Learning.Models.PPO_Neurosymbolic.common.env_util import make_vec_env
from Learning.Models.PPO_Neurosymbolic.PPO_Neurosymbolic import PPO_Neurosymbolic
from Testing.Configuration import env_metrics, test_metrics


def PPO_Neurosymbolic_model(env):
    
    #Metric Imports
    test_metric = test_metrics()
    learning_policy = test_metric.learning_policy
    verbose = test_metric.verbose
    epoches = test_metric.epochs
    learning_rate = test_metric.PPO_Neurosymbolic_learning_rate
    gamma = test_metric.gamma
    batch_size = batch_size.gamma
    
    steps= env_metrics().number_of_steps
    
    #Model Creation
    model = PPO_Neurosymbolic(learning_policy, env, verbose=verbose, learning_rate=learning_rate, n_epochs=epoches, gamma=gamma, batch_size= batch_size)
    
    #Model Training
    model.learn(total_timesteps=steps)
    
    model.save("PPO_Neurosymbolic_cartpole")
    
    del model # remove to demonstrate saving and loading
    
    model = PPO_Neurosymbolic.load("PPO_Neurosymbolic_cartpole")

    obs = env.reset()
    while True:
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)
        env.render("human")
    
    
    
    