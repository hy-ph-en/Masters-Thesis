from Learning.Models.Simple_Reinforcment_Learning import simple_reinforcemeant_learning
from Learning.Models.Simple_Neurosymbolic import simple_neurosymbolic
from Learning.Policy_Grabbers.Symbolic_Regression import symbolic_regression
from Environment.Environment_handler import Environments
from Learning.Models.PPO.ppo_model import ppo_model
from Learning.Models.PPO_Neurosymbolic.ppo_neurosymbolic_model import ppo_neurosymbolic_model

from Testing.Configuration import env_metrics, test_metrics



class learning_handler:
    def __init__(self):
 
        #Configured
        self.env = Environments().environmental_choice()
        
        self.policy = test_metrics().policy
        
        
        #Models
        '1 - simple_reinforcemeant_learning '
        '2 - simple_neurosymbolic           '
        '3 - ppo_model                      '
        '4 - ppo_neurosymbolic              '
        
        #Policy Grabbers
        self.symbolicregression = symbolic_regression()
        
    def model_choice(self):
        #Model
        model = test_metrics().model

        #List of environments
        model_dict = {
            1 : simple_reinforcemeant_learning,
            2 : simple_neurosymbolic,
            3 : ppo_model,
            4 : ppo_neurosymbolic_model
        }
        
        #Default is the simple reinforcement learning model
        return (model_dict.get(model, simple_reinforcemeant_learning))(self.env)
    
    
    def policy_hanlder(self):
        #List of Policies
        policy_dict = {
            1 : self.symbolicregression
        }
        
        
        #Default is to return symbolic regression
        return policy_dict.get(self.policy , self.symbolicregression)