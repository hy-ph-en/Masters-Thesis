# This file is here just to define MlPPO_Neurosymboliclicy/CnnPolicy
# that work for PPO_Neurosymbolic
from Learning.Models.PPO_Neurosymbolic.common.policies import ActorCriticCnnPolicy, ActorCriticPolicy, MultiInputActorCriticPolicy

MlPPO_Neurosymboliclicy = ActorCriticPolicy
CnnPolicy = ActorCriticCnnPolicy
MultiInputPolicy = MultiInputActorCriticPolicy
