n = int(input())
players = [int(x)+1 for x in range(n)]
move1 = [int(x)-1 for x in input().split()]
move2 = [int(x)-1 for x in input().split()]
choice1 = []
choice2 = []
for i in range(n//2):
    choice1.append(players[move1[i]])
    players = players[:move1[i]] + players[move1[i]+1:]
    choice2.append(players[move2[i]])
    players = players[:move2[i]] + players[move2[i] + 1:]
print(*choice1)
print(*choice2)