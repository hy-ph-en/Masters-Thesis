#Function to return what test number it is one and this number would then be used to increment the different file values 




#Function to return a value to say to the config file that it should use the hyperparameter sweep, overriding the prexisiting values given - Done at the bottom of the file


#This should allow for a faster rate of testing as multiple hyparameter combinations can be tried at the same time


#You will need to make it so you can pass in parameters when the program is called, these parameters then change the values here
    #you need to increment the custom value file and the average value file - can do this simply with date and time
#since the files are loaded into memory at compliation time you would need to do multiple executions of the run, this means running a script that recalls the program multiple times
import sys


'#!!#Dont forget that updates will happen one generation ahead, so acocunt for this and conifgure the configuration before the first run with the'
'configurations you want to use#!!#'

def file_overwrite(testing_number, average_file, custom_test_file):

    #So if the value given is True but the current tests are not set up 
    if testing_number == 0:
        metrics_change = {}
    else:
        #Automatic incrementation of the log files to allow for easier inputs
        if average_file =="'Logfile/AverageValue.csv'":
            average_file = "'"+'Logfile/AverageValue'+str(testing_number)+'.csv'+"'"
            print(average_file)
            
        if custom_test_file == "'Logfile/Custom_Run_Averages.csv'":
            custom_test_file = "'"+'Logfile/Custom_Run_Averages'+str(testing_number)+'.csv'+"'"

            print(average_file)
        metrics_change = return_current_test(testing_number, average_file, custom_test_file)

        if metrics_change == True:
            sys.exit(0)

    #Cleaning Files
    with open(('Logfile/Custom_Run_Averages'+str(testing_number)+'.csv'), 'w') as file:
        pass
    with open(('Logfile/Custom_Run_Averages'+str(testing_number)+'.csv'), 'w') as file:
        pass

    with open('Testing/Configuration.py', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        for metric, value in metrics_change.items():
            if line.strip().startswith(f'self.{metric} = '):
                lines[i] = f'        self.{metric} = {value}\n'
                break

    with open('Testing/Configuration.py', 'w') as file:
        file.writelines(lines)


#Storage for hyperparameters
def return_current_test(testing_number, average_file, custom_test_file):
    #For the back to Default 
    file_defaults()

    hyperparameters = {
        3 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroLossPolicy'", 'epochs': 20,'ratio_to_policy': 0.5},
        4 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroLossPolicy'", 'epochs': 20,'ratio_to_policy': 1.25},        
        
        6 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroLossPolicy'", 'epochs': 20,'ratio_to_policy': 1.0, 'neurostep': 250},
        7 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroLossPolicy'",'epochs': 20,'neurostep': 500},

        17 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroPolicy'", 'epochs': 20,'gamma': 0.96},
        18 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroPolicy'", 'epochs': 20,'gamma': 0.97},
        22 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroPolicy'", 'epochs': 20,'gamma': 0.97},


        24 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroLossPolicy'", 'epochs': 20,'complexity': 5},
        27 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroLossPolicy'", 'epochs': 20,'complexity': 19},

        28 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroPolicy'", 'epochs': 20,'complexity': 5},

        40 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroPolicy'", 'epochs': 20,'ppo_learning_rate': 0.0003},
        41 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroPolicy'", 'epochs': 20,'ppo_learning_rate': 0.0005},
    }

    #If the Value Doesnt Exist - Fast Run
    Default = True

    return hyperparameters.get(testing_number, Default)










#Return the to the Default Values
def file_defaults():

    default_metrics = {
        'epochs': 20,
        'gamma': 0.98,
        'clear_data': True,
        'multiple_runs': True,
        'custom_test': True,
        'number_of_runs': 5,
        'epsilon': 0.1,
        'bins': (10, 10),
        'q_learning_rate': 0.9,
        'activation_function': "'ReLU'",
        'ppo_learning_rate': 3e-4,
        'batch_size': 256,
        'learning_policy': "'NeuroPolicy'",
        'verbose': 3,
        'complexity': 20,
        'iterations': 2,
        'neurostep': 1000,
        'precision': 64,
        'ratio_to_policy': 0.5,
        'binary_operators': ["+", "*", "/", "^"],
        'unary_operators': [
            "cos",
            "exp",
            "sin",
            "inv(x) = 1/x",
        ],
        'model': 4,
        'policy': 1,
        'average_file' : "'Logfile/AverageValue.csv'",
        'custom_test_file' : "'Logfile/Custom_Run_Averages.csv'",
        'environment': 6,
        'number_of_envs': 10,
        'number_of_steps': 500000
    }


    with open('Testing/Configuration.py', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        for metric, value in default_metrics.items():
            if line.strip().startswith(f'self.{metric} = '):
                lines[i] = f'        self.{metric} = {value}\n'
                break

    with open('Testing/Configuration.py', 'w') as file:
        file.writelines(lines)


