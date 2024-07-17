from Environment.Environment_handler import Environments
from Learning.Learning_handler import learning_handler
from Testing.Configuration import test_metrics
from Testing.Data_Clearer import clean_csv
from Testing.Average_Value import average_value_loss
from Hyperparameter_Testing import file_overwrite
import random
import argparse

def Run(seed=random.randint(0, 999)):

    #Clear Previous Data
    clean_csv()
    
    learning_handle = learning_handler()
  
    #Policy
    learning_handle.policy_hanlder()
    
    #Model
    learning_handle.model_choice(seed)


def multiple_Runs():
    number_of_runs = test_metrics().number_of_runs
    average_file = test_metrics().average_file
    custom_test_file = test_metrics().custom_test_file

    #Clean Average Value
    if(test_metrics().clear_data):
        with open(average_file, 'w') as file:
            pass
        with open(custom_test_file, 'w') as file:
            pass

    #Also the passed seed value
    for count in range(number_of_runs):
        print("Run Number: ", count)

        #Running Program
        Run(count)

        #Cataloging the Loss Values
        average_value_loss(number_of_runs)


#Taking an input from the computer if available for the hyperparameter
parser = argparse.ArgumentParser(description="Hyperparameter Testing Number")

# Add an argument
parser.add_argument('value', nargs='?', type=int, default=0, help='Hyperparameter Testing Number: ')
parser.add_argument('--string1', type=str, default="'Logfile/AverageValue.csv'", help='First string input.')
parser.add_argument('--string2', type=str, default="'Logfile/Custom_Run_Averages.csv'", help='Second string input.')

testing_inputs = parser.parse_args()

testing_number = testing_inputs.value
average_file = testing_inputs.string1
custom_file = testing_inputs.string2

print(average_file, custom_file)

#Run Type
Multiple = test_metrics().multiple_runs
Custom_test = test_metrics().custom_test
Hyperparameter_Testing = test_metrics().hyperparameter_testing

#Registeration of Custom Environments
Environments().registration()

if Multiple and Custom_test:
    print("Both Multiple and Custom_test are positive : Both Will be Run [Make Sure this is Desired]")

if Hyperparameter_Testing:
    file_overwrite(testing_number, average_file, custom_file)

    #file_overwrite(testing_number, average_file, custom_test_file)

if Multiple:
    multiple_Runs()

else :
    Run()


