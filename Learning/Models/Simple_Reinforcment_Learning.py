import gymnasium as gym
import numpy as np
from Configuration import test_metrics, env_metrics



def simple_reinforcemeant_learning(env):
    #Variables
    episodes = test_metrics.epochs
    learning_rate = test_metrics.number_of_steps
    gamma = 
    epsilon=0.1
    
    
    # Initialize Q table with zeros
    num_states = (env.observation_space.high - env.observation_space.low) * np.array([10, 100])
    num_states = np.round(num_states, 0).astype(int) + 1
    Q = np.random.uniform(low=-1, high=1, size=(num_states[0], num_states[1], env.action_space.n))
    
    # Training loop
    for episode in range(episodes):
        state = discretize_state(env.reset())
        done = False

        while not done:
            # Epsilon-greedy action selection
            if np.random.random() < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(Q[state[0], state[1]])

            # Take action and observe reward and new state
            next_state, reward, done, _ = env.step(action)
            next_state = discretize_state(next_state)

            # Q-learning formula
            best_next_action = np.argmax(Q[next_state[0], next_state[1]])
            td_target = reward + gamma * Q[next_state[0], next_state[1], best_next_action]
            td_error = td_target - Q[state[0], state[1], action]
            Q[state[0], state[1], action] += learning_rate * td_error

            state = next_state
        
        # Optionally print progress
        if episode % 1000 == 0:
            print(f"Episode: {episode}")
    
    return Q

# Helper function to discretize the state
def discretize_state(state):
    state_adj = (state - env.observation_space.low) * np.array([10, 100])
    return np.round(state_adj, 0).astype(int)


def evaluate_policy(env, Q, episodes=100):
    total_rewards = 0

    for _ in range(episodes):
        state = discretize_state(env.reset())
        done = False
        while not done:
            action = np.argmax(Q[state[0], state[1]])
            next_state, reward, done, _ = env.step(action)
            state = discretize_state(next_state)
            total_rewards += reward
            if done:
                break
    
    average_reward = total_rewards / episodes
    print(f"Average reward over {episodes} episodes: {average_reward}")
    return average_reward 