from agent import Agent
import random
from copy import deepcopy
from queue import PriorityQueue
import heapq


class AlphaBetaAgent(Agent):
  
    def __init__(self,game,depth):
        super().__init__(game)
        self.depth = depth
        self.expanded_states = 0
    
    """
    def my_func(self,element):
        polovina = (len(self.game.initial[0])+1)//2

        return abs(element-polovina)
    """

    def decision(self,gameState):
        self.expanded_states = 1
        actions = self.game.get_actions(gameState)
        best_action = random.choice(actions)
        """
        queue = []
        for element in actions:
            heapq.heappush(queue, (self.my_func(element[1]), element))

        
        actions = [element[1] for element in queue]
        """
        maxValue = float('-inf')
        alpha = float('-inf')
        beta = float('+inf')

        print(actions)

        #mozda ove akcije poredjati da budu od najbolje do najgore, kako bismo optimizovali alpha-beta prunning
        for action in actions:
            succState = self.game.apply_action(gameState,action)
            value = self.min_value(succState,0,alpha,beta)
            print("VALUE JE ",value,"ACTION JE ",action)
            if value > maxValue:
                maxValue = value
                best_action = action
        print("Expanded states:",self.expanded_states)
        print(best_action,maxValue)
        

        return best_action
    """
    def decision2(self,gameState):
        self.expanded_states = 1
        actions = self.game.get_actions(gameState)
        best_action = random.choice(actions)
        minValue = float('inf')
        alpha = float('-inf')
        beta = float('+inf')

        for action in actions:
            succState = self.game.apply_action(gameState,action)
            value = self.max_value(succState,-2,alpha,beta)
            print("VALUE JE ",value,"ACTION JE ",action)
            if value < minValue:
                minValue = value
                best_action = action
        print("Expanded states:",self.expanded_states)
        print(best_action,minValue)
        

        return best_action
        """
    

    def max_value(self, currState,currDepth,alpha,beta):
        #print("U MAX JE STANJE TRENUTNO OVO ISPOD",currDepth,"UTILITY U TOM STANJU JE",self.game.get_utility(currState))
        #self.game.display(currState)
        
        if self.game.is_terminal(currState):
            return self.game.get_utility(currState)
            

        if self.game.is_terminal(currState) or currDepth == self.depth:
           # print("MAXVALUE UTILITET",self.game.get_utility(currState))
            return self.game.get_utility(currState)
        

        
        
       


        actions = self.game.get_actions(currState)
        maxValue = float('-inf')

        

        for action in actions:
            succState = self.game.apply_action(currState,action)
            
            
            maxValue = max(maxValue,self.min_value(succState,currDepth,alpha,beta))

            if maxValue >= beta:

                return maxValue
            alpha = max(alpha,maxValue)

        return maxValue
        
    def min_value(self, currState,currDepth,alpha,beta):
        #print("U MIN JE STANJE TRENUTNO OVO ISPOD",currDepth,"UTILITY U TOM STANJU JE",self.game.get_utility(currState))
        #self.game.display(currState)
       
        if self.game.is_terminal(currState) or currDepth == self.depth:
            #print("MINVALUE UTILITET",self.game.get_utility(currState))

            return self.game.get_utility(currState)-currDepth
        

        actions = self.game.get_actions(currState)
        minValue = float('inf')
        
        self.expanded_states+=1
        for action in actions:
            succState = self.game.apply_action(currState,action)

            minValue = min(minValue,self.max_value(succState,currDepth+1,alpha,beta))
            
            if minValue <= alpha:

                return minValue
            beta = min(beta,minValue)

        return minValue
    