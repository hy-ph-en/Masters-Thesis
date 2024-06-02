from Testing.Configuration import test_metrics, env_metrics
from Learning.Models.Simple_Reinforcment_Learning import evaluate_policy
from Testing.Metrics.Q_Learning_Specific import Q_learning_specific

Reinforcement_Learning_models = {
    1 : "Simple Reinforcement Learning Model",
    3 : "PPO"
}

Neurosybolic_models = {
    2 : "Simple Neurosymbolic Learning Model",
    4 : "Neurosymbolic PPO"
}



def Outputs(model,policy=None):
    #Importing Metrics
    env_metric = env_metrics()
    test_metric = test_metrics()

    
    
    
    #Q-learning Specific 
    if(test_metric.model in Reinforcement_Learning_models.keys()):
        if test_metric.model == 1:
            Q_learning_specific(model)
            
        #Default metrics aswell
    elif(Neurosybolic_models in Neurosybolic_models.keys()):
        pass
    else:
        #Default metrics
        pass