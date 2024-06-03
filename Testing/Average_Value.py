import pandas as pd 
import os


#called before the cleaning of the data
#look at the excel sheet for progress and look at the notes for what to do

#first line is a count, everything else is the data

#prob an issue related to the rollout/ep_rew_mean
#something is wrong 

def average_value_loss(number_of_runs=0):
    path_created = 'Logfile/Baseline_Output/progress.csv'

    folder_name = 'Logfile/Baseline_Output'
    file_name = 'progress.csv'
    path_created = os.path.join(folder_name, file_name)

    #maybe try doing the build path thing? using os

    if not csv_is_empty(path_created) and number_of_runs != 0:
        df_created_data = pd.read_csv(path_created).astype(float)
        df_created_data = df_created_data.dropna()

        df_created_data = df_created_data.loc[:, ['train/learning_rate','train/loss', 'train/value_loss', 'rollout/ep_rew_mean']]
        print(df_created_data)

        path_remembered = 'Logfile/AverageValue.csv'

        if not csv_is_empty(path_remembered):
            remebered_data = pd.read_csv(path_remembered).astype(float)
        else:
            first_pass(df_created_data)
            remebered_data = pd.read_csv(path_remembered).astype(float)

        #could be an issue with the df_created_data
        #I think its reading the column and row numbering as numbers it should carry forward, causing it to grow by an increment every run
        #Its reading a row as the incrementation and then adding to it, shifting it across, why tho?

        #Try always dropping the first column of the panda?
        #Can use the count to decrement which one to do?

        #print(remebered_data)



        for line in range(len(df_created_data)):
            #Check if the insertion place is empty

            for column in range(len(df_created_data.columns)):

                remebered_data.iloc[line, column] = remebered_data.iloc[line, column] + (df_created_data.iloc[line, column] /number_of_runs)

        with open('Logfile/AverageValue.csv', 'w') as file:
            pass
        

        remebered_data = remebered_data.drop(remebered_data.columns[0], axis=1)

        remebered_data.to_csv(path_remembered)
        
#First populate all the 0s, then do the dataframe, then pass the modified panda back to the csv 


def first_pass(df_created_data):
    from csv import writer

    folder_name = 'Logfile'
    file_name = 'AverageValue.csv'
    file_path = os.path.join(folder_name, file_name)


    with open(file_path, mode='a', newline='') as dataframe:
        writer_object = writer(dataframe)

        for _ in range(len(df_created_data)+1):
            writer_object.writerow([0,0,0,0])

        dataframe.close()

def csv_is_empty(file_path):
    try:
        df = pd.read_csv(file_path)
        return False
    except pd.errors.EmptyDataError:
        return True




average_value_loss()


