#Function to return what test number it is one and this number would then be used to increment the different file values 




#Function to return a value to say to the config file that it should use the hyperparameter sweep, overriding the prexisiting values given - Done at the bottom of the file


#This should allow for a faster rate of testing as multiple hyparameter combinations can be tried at the same time


#You will need to make it so you can pass in parameters when the program is called, these parameters then change the values here
    #you need to increment the custom value file and the average value file - can do this simply with date and time
#since the files are loaded into memory at compliation time you would need to do multiple executions of the run, this means running a script that recalls the program multiple times



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

    hyperparameters = {
        1 : {'average_file':average_file,'custom_test_file': custom_test_file,'learning_policy': "'NeuroLossPolicy'", 'ratio_to_policy': 0.1},
        2 : {'average_file':average_file,'custom_test_file': custom_test_file, 'ratio_to_policy': 0.25},
        3 : {'average_file':average_file,'custom_test_file': custom_test_file, 'ratio_to_policy': 0.5},
        4 : {'average_file':average_file,'custom_test_file': custom_test_file, 'ratio_to_policy': 1.25},        
        
        6 : {'average_file':average_file,'custom_test_file': custom_test_file, 'ratio_to_policy': 1.0, 'neurostep': 250},#Back to Default
        7 : {'average_file':average_file,'custom_test_file': custom_test_file, 'neurostep': 500},
        8 : {'average_file':average_file,'custom_test_file': custom_test_file, 'neurostep': 2500},
        9 : {'average_file':average_file,'custom_test_file': custom_test_file, 'neurostep': 5000},
        10 : {'average_file':average_file,'custom_test_file': custom_test_file, 'neurostep': 10000},


        11 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroPolicy'", 'neurostep': 250},#Back to Default
        12 : {'average_file':average_file,'custom_test_file': custom_test_file, 'neurostep': 500},
        13 : {'average_file':average_file,'custom_test_file': custom_test_file, 'neurostep': 2500},
        14 : {'average_file':average_file,'custom_test_file': custom_test_file, 'neurostep': 5000},
        15 : {'average_file':average_file,'custom_test_file': custom_test_file, 'neurostep': 10000},

        16 : {'average_file':average_file,'custom_test_file': custom_test_file, 'gamma': 0.95},
        17 : {'average_file':average_file,'custom_test_file': custom_test_file, 'gamma': 0.96},
        18 : {'average_file':average_file,'custom_test_file': custom_test_file, 'gamma': 0.97},
        19 : {'average_file':average_file,'custom_test_file': custom_test_file, 'gamma': 0.99},

        20 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroLossPolicy'",'gamma': 0.95},
        21 : {'average_file':average_file,'custom_test_file': custom_test_file, 'gamma': 0.96},
        22 : {'average_file':average_file,'custom_test_file': custom_test_file, 'gamma': 0.97},
        23 : {'average_file':average_file,'custom_test_file': custom_test_file, 'gamma': 0.99},


        24 : {'average_file':average_file,'custom_test_file': custom_test_file, 'complexity': 5},
        25 : {'average_file':average_file,'custom_test_file': custom_test_file, 'complexity': 10},
        26 : {'average_file':average_file,'custom_test_file': custom_test_file, 'complexity': 15},
        27 : {'average_file':average_file,'custom_test_file': custom_test_file, 'complexity': 19},       #Back to Default

        28 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroPolicy'",'complexity': 5},
        29 : {'average_file':average_file,'custom_test_file': custom_test_file, 'complexity': 10},
        30 : {'average_file':average_file,'custom_test_file': custom_test_file, 'complexity': 15},
        31 : {'average_file':average_file,'custom_test_file': custom_test_file, 'complexity': 19},       #Back to Default

        32 : {'average_file':average_file,'custom_test_file': custom_test_file, 'iterations': 5},
        33 : {'average_file':average_file,'custom_test_file': custom_test_file, 'iterations': 10},

        34 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroLossPolicy'", 'iterations': 5},
        35 : {'average_file':average_file,'custom_test_file': custom_test_file, 'iterations': 10},


        36 : {'average_file':average_file,'custom_test_file': custom_test_file, 'ppo_learning_rate': 0.0002, 'iterations': 2},       #Back to Default
        37 : {'average_file':average_file,'custom_test_file': custom_test_file, 'ppo_learning_rate': 0.0003},
        38 : {'average_file':average_file,'custom_test_file': custom_test_file, 'ppo_learning_rate': 0.0005},

        39 : {'average_file':average_file,'custom_test_file': custom_test_file, 'learning_policy': "'NeuroPolicy'",'ppo_learning_rate': 0.0002},
        40 : {'average_file':average_file,'custom_test_file': custom_test_file, 'ppo_learning_rate': 0.0003},
        41 : {'average_file':average_file,'custom_test_file': custom_test_file, 'ppo_learning_rate': 0.0005},
    }

    return hyperparameters.get(testing_number)










#Return the to the Default Values
def file_defaults():

    default_metrics = {
        'epochs': 20,
        'gamma': 0.98,
        'clear_data': True,
        'multiple_runs': True,
        'custom_test': True,
        'number_of_runs': 3,
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
        'custom_environment_test': 11,
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


