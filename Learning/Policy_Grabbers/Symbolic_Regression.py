#https://github.com/MilesCranmer/PySR
#https://arxiv.org/pdf/2305.01582.pdf

import pysr
from pysr import PySRRegressor
from Testing.Configuration import test_metrics
from matplotlib import pyplot as plt 


class symbolic_reg:
    
    #Initializing Values
    def __init__(self):
        testing_values = test_metrics()
        
        self.niterations = testing_values.iterations
        self.binary_operators = testing_values.binary_operators
        self.unary_operators = testing_values.unary_operators
        self.complexity = testing_values.complexity
    
    
    def symbolic_regression(self,features, predictions):
        
        model = PySRRegressor(
        niterations=self.niterations,
        binary_operators=self.binary_operators,
        unary_operators=self.unary_operators,
        extra_sympy_mappings={"inv": lambda x: 1 / x},
        progress=False,
        verbosity=0,
        elementwise_loss="loss(prediction, target) = (prediction - target)^2",
        # ^ Custom loss function (julia syntax)
        )
        
        model.fit(features, predictions)
        
        found_prediction = model.predict(features)
        
        #print(model.sympy())
        
        return found_prediction