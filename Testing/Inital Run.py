from Environment_hanlder import Environments
from Learning_hanlder import learning_handler
from Metrics_hanlder import Outputs

def Run():
    
    #Policy
    policy = learning_handler.policy_hanlder()
    
    #Model
    model_outcome = learning_handler.model_choice()

    #Outputs
    Outputs()
