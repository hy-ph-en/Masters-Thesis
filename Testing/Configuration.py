
#Metrics to change as needed for Testing - Model Changes
class test_metrics():
    
    def __init__(self):
        #Normal Model Configurations
        self.epochs = 10                        #Number of training periods 
        self.render = False                     #Whether the rendering of the training is shown      
        self.gamma = 0.99                       #Higher values priorities furture benefit in the training cycle
        
        
        #Q Learning Specific                     
        self.epsilon = 0.1
        self.bins = (10,10)                     #Number of states - From continous to discrete 
        self.q_learning_rate = 0.9              #The rate at which learning takes place
        
        
        #Neural Specific 
        self.activation_function = "ReLU"       #The Activation function passed into the neural network
        
        
        #PPO Specific
        self.ppo_learning_rate = 3e-4           #The rate at which learning takes place
        self.batch_size = 64                    #Mini size batch
        
        
        
        #Learning Polies'
        'MlpPolicy - Multi-Layer Perceptron (MLP) Policy                 '
        'CnnPolicy - Convolutional Neural Network                        '
        'MultiInputPolicy - Multi-actor Policy                           '
        'NeuroPolicy - Neurosymbolic Policy                              '
        
        self.learning_policy = "NeuroPolicy"                                          #PPO passed Learning Policy 

        'verbose 0-3  : increasing amounts of explaination for the output'            #Likely become legacy as the project processes
        self.verbose = 3
        
        
        #Neurosymbolic Specific 
        'Complexity 1-10'
        self.complexity = 5                        #Max Complexity of Result
        self.iterations = 40                       #Number of iterations before giving a result
        self.precision = 64                        #How percise the solution should be - 64 Highest
        
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
        'CartPole-v1 - 9    '
        
        #Default
        'Simpliest Environemnt - "CartPole-v1"'
        self.environment = 9
        
        self.number_of_steps = 250000              #The number of steps the agent can take per training period
        
        


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