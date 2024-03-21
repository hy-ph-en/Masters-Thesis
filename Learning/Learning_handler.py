from Learning.Models.Simple_Reinforcment_Learning import simple_reinforcemeant_learning
from Learning.Models.Simple_Neurosymbolic import simple_neurosymbolic
from Learning.Policy_Grabbers.Symbolic_Regression import symbolic_regression
from Environment.Environment_handler import Environments
from Learning.Models.PPO.ppo_model import ppo_model

from Testing.Configuration import env_metrics, test_metrics


#Have to add an SYS 
#Look at the OS libary

class learning_handler:
    def __init__(self):
 
        #Configured
        self.env = Environments().environmental_choice()
        
        test_metric = test_metrics()
        self.policy = test_metric.policy
        
        
        #Models
        self.simple_reinforcement_learning = simple_reinforcemeant_learning(self.env)       #might need to make it a reference to the function rather then the output of the function
        self.simple_neurosymbolic = simple_neurosymbolic(self.env)                          #Just add the models into their own functions and then have the policy handler call on those
        self.ppo_model = ppo_model(self.env)
        
        
        #Policy Grabbers
        self.symbolicregression = symbolic_regression()
        
    def model_choice(self):
        #Model
        model = test_metrics().model

        #List of environments
        model_dict = {
            1 : self.simple_reinforcement_learning,
            2 : self.simple_neurosymbolic,
            3 : self.ppo_model
        }
        
        #Default is the simple reinforcement learning model
        return model_dict.get(model, self.simple_reinforcement_learning)
    
    
    def policy_hanlder(self):
        #List of Policies
        policy_dict = {
            1 : self.symbolicregression
        }
        
        
        #Default is to return symbolic regression
        return policy_dict.get(self.policy , self.symbolicregression)