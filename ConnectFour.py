from copy import deepcopy

class ConnectFour:

    def __init__(self,n,m,color):
        self.color = color
        self.initial = ([],color)
        self.n = n
        self.m = m

        for i in range(n):
            helper = ""
            for j in range(m):
               
                helper+="_"
            
            self.initial[0].append(helper)

        #dictionary za svaku kolonu koliko imam preostalih vrijednosti
    

    def get_actions(self, state):
       
        board = state[0]
        player = state[1]
        actions = []
        n = len(board)
        m = len(board[0])
        index = -1

        for j in range(m):
            index = -1
            for i in range(n-1,-1,-1):
                if board[i][j] == '_':
                    index = i
                    break
            if index!=-1:
                actions.append((index,j,player))
            


        
        return actions
    
    def apply_action(self, state, action):
        resultState = deepcopy(state)
        row, col, player = action
        resultState[0][row] = state[0][row][:col]+player+state[0][row][(col+1):]

        return (resultState[0], 'P' if player=='C' else 'C')
      


    def display(self,state):

        

        for i in range(self.n):
            str = ""
            for j in range(self.m):
                str+=state[0][i][j]+"|"
            
            print(' '.join(str))

    def is_winner(self,state,player):
       
        tabla = state[0]

    
        

       

        for i in range(len(tabla)):
            for j in range(len(tabla[i])-3):

                if tabla[i][j] == tabla[i][j+1] and tabla[i][j] == tabla[i][j+2] and tabla[i][j] == tabla[i][j+3] and tabla[i][j] == player:
                    return True
        
        for i in range(len(tabla[0])):
            for j in range(len(tabla)-3):

                if tabla[j][i] == tabla[j+1][i] and tabla[j][i] == tabla[j+2][i] and tabla[j][i] == tabla[j+3][i] and tabla[j][i] == player:
                    return True
            
        # za svako polje provjeriti po dijagonalama

        for i in range(len(tabla)-3):
            for j in range(len(tabla[i])-3):
                if tabla[i][j] == tabla[i+1][j+1] and tabla[i][j] == tabla[i+2][j+2] and tabla[i][j] == tabla[i+3][j+3] and tabla[i][j] == player:
                    return True
        

        for i in range(len(tabla)-3):
            for j in range(len(tabla[i])-1,2,-1):

                if tabla[i][j] == tabla[i+1][j-1] and tabla[i][j] == tabla[i+2][j-2] and tabla[i][j] == tabla[i+3][j-3] and tabla[i][j] == player:
                    return True
        
        return False
    
    def is_terminal(self, state):
        if self.is_winner(state, 'P') or self.is_winner(state, 'C'):
            return True
        
        board = state[0]
        
        val = 0

        for i in range(len(board)):
            val+=board[i].count("_")
    
        return val == 0
    

                

   

   

    def get_utility(self,state):

        if self.is_winner(state, 'P') and self.color == 'P':
            return 10**20
        elif self.is_winner(state, 'C') and self.color == 'P':
            return -(10**20)
        elif self.is_winner(state,'P') and self.color == 'C':
            return -10**20
        
        elif self.is_winner(state,'C') and self.color == 'C':
            return 10**20
        
        elif self.is_terminal(state):
            return 0
        
        value = 0
        board = state[0]
        n = len(board)
        m = len(board[0])
        player = state[1]
        #print("---------------------------")
        #print("TRENUTNO STANJE JE","UTLITET JE ",self.get_utility2(state))
        #self.display(state)
        #print("---------------------------")
        
        
        #za 3(hor 70 35 vert 130  diag=1 1) za 2(hor 25 13 vert 35 diag 13 113) za 1(hor 7 1 vert 13 diag 3.5 1)
       

        for i in range(n):
            for j in range(m-3):
                str = board[i][j]+board[i][j+1]+board[i][j+2]+board[i][j+3]

                if str.count('C') == 3 and str.count('_') == 1:
                    value-=32.5

                if str.count('P') == 3 and str.count('_') == 1:
                    value+=60

                    
                    
                  

                if str.count('P') == 2 and str.count('_') == 2:
                    value+=6.5

                
                    


                if str.count('C') == 2 and str.count('_') == 2 :
                    value-=4.5
                    
                    

                if str.count('P') == 1 and str.count('_') == 3:
                    value+=1
                    
                   
                    
                if str.count('C') == 1 and str.count('_') == 3 :
                    value-=1
                    
                    
                
                
        for i in range(n):
            for j in range(3,m):
                str = board[i][j]+board[i][j-1]+board[i][j-2]+board[i][j-3]

                if str.count('C') == 3 and str.count('_') == 1:
                    value-=32.5

                  

                if str.count('P') == 3 and str.count('_') == 1:
                    value+=60

                    
                    
                  

                if str.count('P') == 2 and str.count('_') == 2:
                    value+=6.5

                
                    


                if str.count('C') == 2 and str.count('_') == 2 :
                    value-=4.5
                    
                    

                if str.count('P') == 1 and str.count('_') == 3:
                    value+=1
                    
                   
                    
                if str.count('C') == 1 and str.count('_') == 3 :
                    value-=1
                    
               
                
        for j in range(m):
            for i in range(n-1,2,-1):
                str = board[i][j]+board[i-1][j]+board[i-2][j]+board[i-3][j]
                

                if str.count('C') == 3 and str.count('_') == 1:
                    value-=32.5

                  


                if str.count('P') == 3 and str.count('_') == 1:
                   value+=60

                if str.count('P') == 2 and str.count('_') == 2:
                    value+=6.5

                

                if str.count('C') == 2 and str.count('_') == 2:
                    value-=4.5
                    
                
                if str.count('P') == 1 and str.count('_') == 3:
                    value+=1
                    

                if str.count('C') == 1 and str.count('_') == 3:  
                    value-=1
                    
                    
                
        for j in range(m-3):
            for i in range(3,n):
                str = board[i][j]+board[i-1][j+1]+board[i-2][j+2]+board[i-3][j+3]
                
                if str.count('C') == 3 and str.count('_') == 1:
                    value-=32.5
                  
                   

                if str.count('P') == 3 and str.count('_') == 1:
                    value+=60
                    
                   
                if str.count('P') == 2 and str.count('_') == 2:
                    value+=6.5

                
                    
                 
                if str.count('C') == 2 and str.count('_') == 2 :
                    value-=4.5

                    
                    

                if str.count('P') == 1 and str.count('_') == 3:
                    value+=1
                    
                    
                if str.count('C') == 1 and str.count('_') == 3:
                    value-=1
                    
                    
                
                
        for j in range(3,m):
            for i in range(3,n):
                str = board[i][j]+board[i-1][j-1]+board[i-2][j-2]+board[i-3][j-3]

                if str.count('C') == 3 and str.count('_') == 1:
                    
                    value-=32.5


                if str.count('P') == 3 and str.count('_') == 1:
                    value+=60
                    

                if str.count('P') == 2 and str.count('_') == 2:
                    value+=6.5
                
   
                if str.count('C') == 2 and str.count('_') == 2:
                    value-=4.5
                    
          
                if str.count('P') == 1 and str.count('_') == 3:
                    value+=1
                    
  
                if str.count('C') == 1 and str.count('_') == 3:
                    value-=1
                    
                    
               
        return value if self.color == 'P' else -value
            
        
                


        


        
        
    

        

        

       
        


