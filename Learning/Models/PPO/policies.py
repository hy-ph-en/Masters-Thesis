# This file is here just to define MlpPolicy/CnnPolicy
# that work for PPO
from Learning.Models.common.policies import ActorCriticCnnPolicy, ActorCriticPolicy, MultiInputActorCriticPolicy, NeurosymbolicActorPolicy, NeurosymbolicActorLoss, NeurosymbolicActorJustLoss

MlpPolicy = ActorCriticPolicy
CnnPolicy = ActorCriticCnnPolicy
MultiInputPolicy = MultiInputActorCriticPolicy
NeuroPolicy = NeurosymbolicActorPolicy
NeuroLossPolicy = NeurosymbolicActorLoss
NeuroJustLossPolicy =  NeurosymbolicActorJustLoss
