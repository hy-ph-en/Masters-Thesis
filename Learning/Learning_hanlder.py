from Simple_Reinforcment_Learning import simple_reinforcemeant_learning
from Simple_Neurosymbolic import simple_neurosymbolic
from Symbolic_Regression import symbolic_regression
from Environment_hanlder import env_metrics


class learning_handler:
    def __init__(self):
        #Configured
        self.env = env_metrics.environmental_choice()
        
        #Models
        self.simple_reinforcement_learning = simple_reinforcemeant_learning(self.env)
        self.simple_neurosymbolic = simple_neurosymbolic(self.env)
        
        #Policy Grabbers
        self.symbolicregression = symbolic_regression()
        
    def model_choice(self, model):
        #List of environments
        model_dict = {
            1 : self.simple_reinforcement_learning,
            2 : self.simple_neurosymbolic
        }
        
        #Default is the simple reinforcement learning model
        return model_dict.get(model, self.simple_reinforcement_learning)
    
    
    def policy_hanlder(self, policy):
        #List of Policies
        policy_dict = {
            1 : self.symbolicregression
        }
        
        
        #Default is to return symbolic regression
        return policy_dict.get(policy, self.symbolicregression)
        
    
    
    
    