from Testing.Configuration import test_metrics
import csv
import os

def clean_csv():
    
    if(test_metrics().clear_data):
        with open('Logfile\Drift_data.csv', 'w') as file:
            pass
        with open('Logfile\Weight_Updates.csv', 'w') as file:
            pass
        with open('Logfile\Percentage_Success.csv', 'w') as file:
            pass

