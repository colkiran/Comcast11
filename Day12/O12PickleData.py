
import pickle

ply1 = {'name': 'Sachin Tendulkar', 'runs': 156, 'oppn': 'Australia', 'venue': 'Gabba', 'year': 2008}
ply2 = {'name': 'Rahul Dravid', 'runs': 126, 'oppn': 'England', 'venue': 'Lords', 'year': 2005}

print(f"ply1 :{ply1}")
print(type(ply1))
print(f"ply2 :{ply2}")
print(type(ply2))
players = {}
players['player1'] = ply1
players['player2'] = ply2

FP = open("PlayersData", "ab")              # ab - append and binary
pickle.dump(players, FP)
FP.close()
