Masters Thesis : Worked on during my time at Imperial, revolving around Neurosymbolic AI in Reinforcement Learning
================================================================================================================ 
This project integrates symbolic regression into reinforcement learning to enhance both interpretability and generalizability of learned policies.

It introduces three novel algorithms - SLMA (Symbolic Loss Modification Algorithm), SPUA (Symbolic Policy Update Algorithm), and SLPU (Symbolic Loss and Policy Update) - that modify PPO (Proximal Policy Optimization) to achieve more interpretable and generalizable solutions. 

Key Features 
* Integration of symbolic regression during reinforcement learning training 
* Multiple algorithm implementations with different approaches to symbolic integration 
* Framework for testing in Gymnasium environments
* Customizable hyperparameters for balancing symbolic and neural components 
* Support for measuring interpretability and generalization metrics 

Algorithms 
===================================================================== 
SLMA: Modifies loss function using symbolic regression output 

SPUA: Directly updates policies using symbolic regression 

SLPU: Combines both approaches for potential benefits of each 

Dependencies
====================================================================== 
Stable Baselines3 

PySR (Python Symbolic Regression) 

Gymnasium 

Gym

Python 3.11
