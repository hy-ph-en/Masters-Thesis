
#Metrics to change as needed for Testing - Model Changes
class test_metrics():
    
    def __init__(self):
        #Normal Model Configurations
        self.epochs = 50                        #Number of training periods 
        self.render = False                     #Whether the rendering of the training is shown      
        self.gamma = 0.99                       #Higher values priorities furture benefit in the training cycle
        
        self.clear_data = True                  #Each run the relavent csv files will be cleared of their previous data
        
        
        #Q Learning Specific                     
        self.epsilon = 0.1
        self.bins = (10,10)                     #Number of states - From continous to discrete 
        self.q_learning_rate = 0.9              #The rate at which learning takes place
        
        
        #Neural Specific 
        self.activation_function = "ReLU"       #The Activation function passed into the neural network
        

        
        #PPO Specific
        self.ppo_learning_rate = 3e-4           #The rate at which learning takes place     -3e-4
        self.batch_size = 256                   #Mini size batch    Nominal-64
        
        
        #Learning Polies'
        'MlpPolicy - Multi-Layer Perceptron (MLP) Policy                 '
        'CnnPolicy - Convolutional Neural Network                        '
        'MultiInputPolicy - Multi-actor Policy                           '
        'NeuroPolicy - Neurosymbolic Policy                              '
        'NeuroLossPolicy - Neurosymbolic Policy Loss                     '
        
        self.learning_policy = "NeuroLossPolicy"                                          #PPO passed Learning Policy 

        'verbose 0-3  : increasing amounts of explaination for the output'            #Likely become legacy as the project processes
        self.verbose = 3
        
        
        #Neurosymbolic Specific 
        'Complexity 1-20'
        self.complexity = 19                       #Max Complexity of Result
        self.iterations = 2                        #Number of iterations before giving a result
        self.neurostep = 1000                      #How many stpes the program should run through before preforming symbolic regression
        'Percision 1-64'
        self.precision = 64                        #How percise the solution should be
        
        #-Operators-
        'Binary Operators - "+", "*", "/"       '
        self.binary_operators = ["+", "*", "/"]
        'Unary Operators  - "cos", "exp", "sin" '
        self.unary_operators =  [
            "cos",
            "exp",
            "sin",
            "inv(x) = 1/x",
        ]
        
        
        #Model Choice
        'Simple Reinforcement Learning Model - 1   '
        'Simple Neurosymbolic Learning Model - 2   '
        'PPO Model - 3                             '
        'PPO Neurosymbolic Model - 4               '
        self.model = 4


        #Policy Choice
        'Symbolic Regression PSYR - 1                   '
        self.policy = 1
        



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
        
        #Default
        'Simpliest Environemnt - "CartPole-v1"'
        self.environment = 6
        

        self.number_of_steps = 500000              #The number of steps the agent can take per training period  - CartPole default is 250000
        
        


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