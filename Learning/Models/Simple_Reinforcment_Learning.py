import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
import pickle

from Testing.Configuration import test_metrics, env_metrics
from Environment.Environment_handler import Environments



def simple_reinforcemeant_learning(environment_object):
    return 1
    metrics = test_metrics()
    
    #Variables
    episodes = metrics.epochs
    learning_rate = metrics.learning_rate
    gamma = metrics.gamma
    epsilon = metrics.epsilon
    bins = metrics.bins 
    
    env = environment_object.environment()
    
    epsilon_decay_rate = 2/episodes
    
    # Initialize the Q-table
    Q = init_q_table(env, bins=bins)
    
    rewards_per_episode = np.zeros(episodes)

    for episode in range(episodes):
        current_state = discretize_space(env.observation_space.low, env.observation_space.high, bins, env.reset())
        done = False

        #maybe do steps instead
        while not done:
            # Epsilon-greedy action selection
            if np.random.random() < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(Q[current_state])

            # Take action
            next_state_raw, reward, done, _ , __= env.step(action)        #Outcomes of Action
            next_state = discretize_space(env.observation_space.low, env.observation_space.high, bins, next_state_raw)

            # Update Q-table
            future_optimal_value = np.max(Q[next_state])
            learned_value = reward + gamma * future_optimal_value
            Q[current_state + (action,)] += learning_rate * (learned_value - Q[current_state + (action,)])

            current_state = next_state
        #Counter
        print("Episode", episode)
        
        epsilon = max(epsilon - epsilon_decay_rate, 0)
        rewards_per_episode[episode] = reward
    
    mean_rewards = np.zeros(episodes)
    for t in range(episodes):
        mean_rewards[t] = np.mean(rewards_per_episode[max(0, t-100):(t+1)])
    plt.plot(mean_rewards)
    plt.savefig(f'environment_run.png')

    return Q


#Table of recorded actions
def init_q_table(env, bins=(10, 10), action_size=None):
    """
    Initializes the Q-table with an extra dimension for the actions.
    """
    if action_size is None:
        action_size = env.action_space.n
    
    state_space_bins = bins + (action_size,)
    q_table = np.random.uniform(low=-1, high=1, size=state_space_bins)
    return q_table

#Creating discrete space from the continous space 
def discretize_space(low, high, bins, samples):
    """
    Discretizes a continuous space.
    """
    samples = samples[0] 
    delta = (high - low) / bins
    discrete_samples = np.floor((samples - low) / delta).astype(int)
    discrete_samples = np.clip(discrete_samples, 0, min(bins) - 1)

    return tuple(discrete_samples)


#Evaluating outcome policy
def evaluate_policy(Q):
    """
    Evaluates the learned policy using the Q-table.
    """
    test_metric = test_metrics()
    
    episodes = test_metric.epochs
    bins = test_metric.bins
    
    env = Environments().environmental_choice() #Getting Mountain Car Object
    env = env.environment()                     #Initialising environment

    total_rewards = 0
    
    print("Outcomes")

    for _ in range(episodes):
        state = discretize_space(env.observation_space.low, env.observation_space.high, bins, env.reset())
        done = False

        while not done:
            action = np.argmax(Q[state])
            next_state_raw, reward, done, __ , ___ = env.step(action)
            state = discretize_space(env.observation_space.low, env.observation_space.high, bins, next_state_raw)
            total_rewards += reward

    average_reward = total_rewards / episodes
    print(f"Average reward over {episodes} episodes: {average_reward}")
    return average_reward