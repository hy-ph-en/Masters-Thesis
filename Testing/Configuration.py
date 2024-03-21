
#Metrics to change as needed for Testing - Model Changes
class test_metrics():
    
    def __init__(self):
        #Normal Model Configurations
        self.epochs = 25000                       #Number of training periods 
        self.render = False                     #Whether the rendering of the training is shown
        self.learning_rate = 0.9                #The rate at which learning takes place
        
        
        #Q Learning Specific
        self.gamma = 0.99                       
        self.epsilon = 0.1
        self.bins = (10,10)                     #Number of states - From continous to discrete 
        
        
        #Neural Specific 
        self.activation_function = "ReLU"       #The Activation function passed into the neural network
        
        
        #PPO Specific
        
        #Learning Polies'
        'MlpPolicy - Multi-Layer Perceptron (MLP) Policy                 '
        'CnnPolicy - Convolutional Neural Network                        '
        'MultiInputPolicy - Multi-actor Policy                           '
        
        self.learning_policy = "MlpPolicy"                                          #PPO passed Learning Policy 
        'verbose 0-3  : increasing amounts of explaination for the output'          #Likely become legacy as the project processes
        self.verbose = 1
        
        
        #Neurosymbolic Specific 
        
        
        #Model Choice
        'Simple Reinforcement Learning Model - 1   '
        'Simple Neurosymbolic Learning Model - 2   '
        'PPO Model - 3                             '
        'PPO Neurosymbolic Model - 4               '
        self.model = 3


        #Policy Choice
        'Symbolic Regression - 1                   '
        self.policy = 1
        
        #The Complexity in the Created Outcome
        'Complexity in Solution  1-10              '
        self.complexity = 5
        



#A unified place to change environmental metrics - Environment Changes
class env_metrics():
    
    def __init__(self):        
        #Environment to Run
        'mountain_car - 1   '
        'noisy_road_2d - 2  '
        'noisy_road - 3     '
        'obstacle - 4       '
        'obstacle2 - 5      '
        'pendulum - 6       '
        'road_2d - 7        '
        'road - 8           '
        #Default
        'mountain_car - 1'
        self.environment = 1
        
        self.number_of_steps = 1000              #The number of steps the agent can take per training period
        
        


#Adding More to the Framework
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#Model
'Add the File Models                                                           '
'Need to add the Model to the Learning Handler                                 '

#Policy
'Add the File to Policy Grabbers                                               '
'Need to add the Model to the Learning Handler                                 '

#Environment 
'Add the File to Environemnts'
'Need to add the environment to the Environment_hanlder                         '


#Other Modifcations
'Are Generally Semantic Without Breaking the Framework itself                   '
'Additional inputs can be added in this file if required for the added model    '