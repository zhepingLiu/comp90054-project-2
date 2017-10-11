def getReward(agent, gameState, prevState, terminal):
    if terminal:
        if agent.getScore(gameState) == 0:
            return -1000
        else: return agent.getScore(gameState) * 1000
    else:
        r = (agent.getScore(gameState) - agent.prevScore) * 50
        x, y = gameState.getAgentPosition(agent.index)
        if agent.getFood(prevState)[x][y]:
            # ate food
            r += 10
        if agent.prevIsIllegal:
            # had invalid action in last step
            r -= 10
        prevX, prevY = prevState.getAgentPosition(agent.index)
        if (abs(prevX - x) + (prevY - y)) > 1:
            # ate by opponent
            r -= 50
        r -= 1 # time
        print("reward: {}".format(r))
        return r