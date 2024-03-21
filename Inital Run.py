from Environment.Environment_handler import Environments
from Learning.Learning_handler import learning_handler
from Testing.Metrics.Metrics_hanlder import Outputs

def Run():
    
    learning_handle = learning_handler()
    
    #Policy
    policy = learning_handle.policy_hanlder()
    
    #Model
    model_outcome = learning_handle.model_choice()

    #Outputs
    Outputs(model_outcome,policy)


Run()