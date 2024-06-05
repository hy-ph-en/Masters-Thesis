from Environment.Environment_handler import Environments
from Learning.Learning_handler import learning_handler
from Testing.Configuration import test_metrics
from Testing.Metrics.Metrics_hanlder import Outputs
from Testing.Data_Clearer import clean_csv
from Testing.Average_Value import average_value_loss
import random

def Run(seed=random.randint(0, 999)):

    #Clear Previous Data
    clean_csv()
    
    learning_handle = learning_handler()
  
    #Policy
    policy = learning_handle.policy_hanlder()
    
    #Model
    model_outcome = learning_handle.model_choice(seed)
    
    #Outputs
    #Outputs(model_outcome,policy)



#Run Type
Multiple = test_metrics().multiple_runs

if Multiple:
    number_of_runs = test_metrics().number_of_runs

    #Clean Average Value
    if(test_metrics().clear_data):
        with open('Logfile/AverageValue.csv', 'w') as file:
            pass

    #Also the passed seed value
    for count in range(number_of_runs):
        print("Run Number: ", count)

        #Running Program
        Run(count)

        #Cataloging the Loss Values
        average_value_loss(number_of_runs)

else :
    Run()