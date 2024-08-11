import numpy as np
class Agent:

    def __init__(self, game):
        self.game = game
    
    def decision(self, gameState):
        actions = self.game.get_actions(gameState)
        return actions[np.random.choice(range(len(actions)))]


    def validna(self,kolona,gameState):
        index = -1
        board = gameState[0]

        n = len(board)

        for i in range(n-1,-1,-1):
            if board[i][kolona] == '_':
                return i
        
        return -1


    
    def play(self):

        gameState = self.game.initial
        
       

            # potez agenta
       
        
        while not self.game.is_terminal(gameState):
              
              validMove = False
             
              while not validMove:
                move = input("Odaberite kolonu: ")
                
                
                

                if move.isnumeric() and int(move) > 0 and int(move) <= len(gameState[0][0]):
                    
                    kolona = int(move)
                    
                  
                    
                    if self.validna(kolona-1,gameState)!=-1:
                        validMove = True
                        opponentColor = 'C' if self.game.color == 'P' else 'P'
                        userAction = (self.validna(kolona-1,gameState),kolona-1,opponentColor)
                        
                        gameState = self.game.apply_action(gameState, userAction)
                        self.game.display(gameState)
                       
            

              agentAction = self.decision(gameState)
            
              gameState = self.game.apply_action(gameState, agentAction)
              self.game.display(gameState)

              

            
           # userAction = self.decision2(gameState)
            
            #if self.game.is_terminal(gameState):
             #   break
           
            
            #gameState = self.game.apply_action(gameState,userAction)
            #self.game.display(gameState)
           

              if self.game.is_terminal(gameState):
                 break
            
            
            # potez korisnika
            
                                           
                        

        if self.game.is_winner(gameState, 'P'):
            print("P wins!")
        elif self.game.is_winner(gameState, 'C'):
            print("C wins!")
        else:
            print("Draw")
       