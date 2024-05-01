from Environment.Environment_handler import Environments
from Learning.Learning_handler import learning_handler
from Testing.Metrics.Metrics_hanlder import Outputs
from Testing.Data_Clearer import clean_csv

def Run():

    #Clear Previous Data
    clean_csv()
    
    learning_handle = learning_handler()
  
    #Policy
    policy = learning_handle.policy_hanlder()
    
    #Model
    model_outcome = learning_handle.model_choice()
    
    #Outputs
    Outputs(model_outcome,policy)


Run()