
#Metrics to change as needed for Testing - Model Changes
class test_metrics():
    
    def __init__(self):
        #Normal Model Configurations
        self.epochs = 1
        self.render = False                     #Whether the rendering of the training is shown      
        self.gamma = 0.98
        
        self.clear_data = True
        self.multiple_runs = True
        self.custom_test = True
        self.hyperparameter_testing = True
        self.number_of_runs = 2
        
        #Q Learning Specific                     
        self.epsilon = 0.1
        self.bins = (10, 10)
        self.q_learning_rate = 0.9
        
        
        #Neural Specific 
        self.activation_function = 'ReLU'
        

        #PPO Specific
        self.ppo_learning_rate = 0.0005
        self.batch_size = 256
        
        
        #Learning Polices'
        'MlpPolicy - Multi-Layer Perceptron (MLP) Policy                 '
        'CnnPolicy - Convolutional Neural Network                        '
        'MultiInputPolicy - Multi-actor Policy                           '
        'NeuroPolicy - Neurosymbolic Policy                              '
        'NeuroLossPolicy - Neurosymbolic Policy and Loss                 '
        'NeuroJustLossPolicy - Neurosymbolic Loss                        '
        
        self.learning_policy = 'NeuroJustLossPolicy'

        'verbose 0-3  : increasing amounts of explaination for the output'            #Likely become legacy as the project processes
        self.verbose = 3
        
        
        #Neurosymbolic Specific 
        'Complexity 1-20'
        self.complexity = 20
        self.iterations = 2
        self.neurostep = 100
        'Percision 1-64'
        self.precision = 64
        self.ratio_to_policy = 0.5
        
        #-Operators-                               #Balance between more operators allowing for a more emblematic solution and more opertors meaning a higher computational time
        'Binary Operators - "+", "*", "/"       '
        self.binary_operators = ['+', '*', '/', '^']
        'Unary Operators  - "cos", "exp", "sin" '
        self.unary_operators = ['cos', 'exp', 'sin', 'inv(x) = 1/x']

        #Model Choice
        'Simple Reinforcement Learning Model - 1            Legacy'
        'Simple Neurosymbolic Learning Model - 2            Legacy'
        'PPO Model - 3                             '
        'PPO Neurosymbolic Model - 4               '
        self.model = 4


        #Policy Choice
        'Symbolic Regression PSYR - 1                   '
        self.policy = 1

        #Filenames
        self.average_file = 'Logfile/AverageValue41.csv'
        self.custom_test_file = 'Logfile/Custom_Run_Averages41.csv'
        



#A unified place to change environmental metrics - Environment Changes
class env_metrics():
    
    def __init__(self):        
        #Environment to Run
        'MountainCar - 1   '
        'noisy_road_2d - 2  '
        'noisy_road - 3     '
        'obstacle - 4       '
        'obstacle2 - 5      '
        'Pendulum - 6       '
        'road_2d - 7        '
        'road - 8           '
        'CartPole-v1 - 9    '
        'MountainCar Success- 10  '
        'Pendulum Length - 11'
        'Pendulum Length Extended - 12'
        'Pendulum Gravity - 13'
        'Pendulum Gravity Increased - 14'
        
        #Default
        'Simpliest Environemnt - "CartPole-v1"'
        self.environment = 6
        
        #Custom Environments - Testing
        self.custom_environment_test = 11

        self.custom_environment_test_one = 12

        self.custom_environment_test_two = 13

        self.custom_environment_test_three = 14

        #Environment Configurations
        self.number_of_envs = 10

        self.number_of_steps = 500000

        self.number_of_custom_envs = 4
        
        


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
