from ConnectFour import ConnectFour
from alphabeta_agent import AlphaBetaAgent
from agent import Agent



n = int(input("Unesite broj vrsta: "))

m = int(input("Unesite broj kolona: "))
color = input("Unesite boju za agenta: ")

while color!='C' and color!='P':
    color = input("Unesite boju za agenta: ")


game = ConnectFour(n,m,color)

a = AlphaBetaAgent(game,depth = 3)

a.play()

"""
xddd = ([],"P")

for i in range(6):
    str = ""
    for j in range(7):
        if j == 3:
            if i%2 == 0:
                str+="C"
            else:
                str+="P"
        elif j == 1:
           
            if i == 5:
                str+="C"
            else:
                str+="_"
        elif j == 2:
            if i == 5:
                str+="P"
            
            else:
                str+="_"
        elif j == 5:
            if i == 5:
                str+="P"
            else:
                str+="_"
        else:
            str+="_"
    xddd[0].append(str)


game.display(xddd)

print(game.get_utility(xddd))
"""




