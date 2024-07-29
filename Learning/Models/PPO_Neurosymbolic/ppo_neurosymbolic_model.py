from csv import writer
import os
from Learning.Models.common.env_util import make_vec_env
from Learning.Models.PPO_Neurosymbolic.ppo import PPO
from Testing.Configuration import env_metrics, test_metrics
from Learning.Models.common.logger import configure
from Environment.Environment_handler import Environments
from Learning.Models.common.evaluation import evaluate_policy

import torch


def ppo_neurosymbolic_model(env, seed):
    
    #Metric Imports
    test_metric = test_metrics()
    learning_policy = test_metric.learning_policy
    verbose = test_metric.verbose
    epoches = test_metric.epochs
    learning_rate = test_metric.ppo_learning_rate
    gamma = test_metric.gamma
    batch_size = test_metric.batch_size
    
    steps= env_metrics().number_of_steps

    #GPU Acceleration
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    #Model Creation
    model = PPO(learning_policy, env, seed=seed, verbose=verbose, learning_rate=learning_rate, n_epochs=epoches, gamma=gamma, batch_size= batch_size, device="cpu")

    tmp_path = "Logfile/Baseline_Output"

    new_logger = configure(tmp_path, ["csv"])

    model.set_logger(new_logger)
    
    #Model Training
    model.learn(total_timesteps=steps)
    
    #Model Output
    if not test_metric.multiple_runs and not test_metric.custom_test:
        model.save("Environment_Solution")
    
        del model # remove to demonstrate saving and loading

        run_model_loop(env)

    if test_metric.custom_test:
        model.save("Environment_Solution")

        del model
    
        run_custom_loop()

#Run the Trained Model over a change in the Environment to Oberserve the Outcome 
def run_custom_loop():
    model = PPO.load("Environment_Solution")
    number_of_envs = env_metrics().number_of_custom_envs
    
    for custom_number in range(number_of_envs):
        print(custom_number)
        env = Environments().environmental_choice(custom_run=True, custom_number=custom_number)

        mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10)

        file_path = test_metrics().custom_test_file

        with open(file_path, mode='a', newline='') as dataframe:
            writer_object = writer(dataframe)
                            
            writer_object.writerow([mean_reward,std_reward])

            dataframe.close()



    with open(file_path, mode='a', newline='') as dataframe:
        writer_object = writer(dataframe)

        writer_object.writerow([])

        dataframe.close()

    
        

#Continue Running the Simulation Until Manually Broken
def run_model_loop(env):
    model = PPO.load("Environment_Solution")
    obs = env.reset()
    while True:
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)

        env.render("human")