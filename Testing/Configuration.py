
#Metrics to change as needed for Testing - Model Changes
class test_metrics():
    
    def __init__(self):
        #Normal Model Configurations
        self.epochs = 5000                      #Number of training periods 
        self.render = False                     #Whether the rendering of the training is shown
        self.learning_rate = 0.9                #The rate at which learning takes place
        self.gamma = 
        
        #Neural Specific 
        self.activation_function = "ReLU"       #The Activation function passed into the neural network
        
        
        #Neurosymbolic Specific 
        
        
        #Model Choice
        'Simple Reinforcement Learning Model - 1   '
        'Simple Neurosymbolic Learning Model - 2   '
        self.model = 1


        #Policy Choice
        'Symbolic Regression - 1                   '
        self.policygrabber = 1
        
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
        
        
