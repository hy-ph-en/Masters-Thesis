# This file is here just to define MlpPolicy/CnnPolicy
# that work for PPO
from Learning.Models.PPO_Neurosymbolic.common.policies import ActorCriticCnnPolicy, ActorCriticPolicy, MultiInputActorCriticPolicy

MlpPolicy = ActorCriticPolicy
CnnPolicy = ActorCriticCnnPolicy
MultiInputPolicy = MultiInputActorCriticPolicy
