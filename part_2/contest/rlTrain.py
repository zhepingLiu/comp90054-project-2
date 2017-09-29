import sys
import util
import featuresTool

alpha = 0.1 # learning rate

# def extractFeatures(state, action, nextState, agent,featureTool):
#     # return features of state
#     temp = featureTool.getFeatures(agent,state,action,nextState)
#     res = [temp[line] for line in featureTool.dict]
#     return temp
#     pass

def extractFeatures(agent, states, actions):
    """
    Extract features of a game for a agent
    agent - CaptureAgent object
    states - list of states of that agent in the game,
             states[0] is the initial state,
             states[-1] is the outcome (one of "Win", "Lose", "Tie")
    actions - list of actions the agent performed at each corresponding state
              actions[-1] = None
    return - list of features corresponding to each given state
    """
    #print states
    
    tool = featuresTool.featuresTool()
    tool.initGame(agent,states[0])
    
    features = []
    
    for i in range(len(states)-1):
        features.append(tool.getTrainSet(agent,states[i],actions[i],None))
    
    features.append([0])
    
    return features

def train(features, actions, labels, model = "Linear"):
    # return trained weights
    return 0
    if model == "Linear":
        return trainLinear(features, labels)
    else:
        print "Undefined model"
        sys.exit(1)

def trainLinear(features, labels):
    # initialize weights
    weights = util.Counter()
    # stochastic gradient descent
    for i in len(labels):
        diff = labels[i] - features[i] * weights
        for feature, value in features[i].iteritems():
            weights[feature] += alpha * diff * value
    return weights