
players = {
    'sachin': [290, 350, 410, 320, 435],
    'sehwag': [340, 450, 410, 390, 400],
    'rahul' : [180, 230, 385, 275, 200],
    'sourav': [190, 330, 230, 305, 150],
    'yuvraj': [150, 185, 250, 320, 160],
    'laxman': [175, 158, 335, 225, 140]
}

print(f"players :{players}")
print("sachin :", players['sachin'])
print("sachin :", sum(players['sachin']))

print("-" * 40)

plyr_scr = {k for k in players}
print(f"plyr_scr :{plyr_scr}")

print("-" * 40)
plyr_scr = {k for k in players.keys()}
print(f"plyr_scr :{plyr_scr}")

print("-" * 40)
plyr_scr = [v for v in players.values()]
print(f"plyr_scr :{plyr_scr}")

print("-" * 40)
plyr_scr = {k: v for k, v in players.items()}
print(f"plyr_scr :{plyr_scr}")

print("-" * 40)
plyr_scr = {k: sum(v) for k, v in players.items()}
print(f"plyr_scr :{plyr_scr}")

print("-" * 40)
plyr_scr = {k: (lambda score: sum(score) / len(score))(v)
            for k, v in players.items()}
print(f"plyr_scr :{plyr_scr}")

print("-" * 40)
scrs = [score for score in players.values()]
print(f"scrs :{scrs}")

print("-" * 40)
scrs = [scr for score in players.values() for scr in score]
print(f"scrs :{scrs}")

print("-" * 40)
scrs = [scr for score in players.values() for scr in score if scr >= 200]
print(f"scrs :{scrs}")

print("-" * 40)
scrsGT200 = {name :[scr for scr in score if scr >= 200]
             for name, score in players.items()}
print(f"Scores Greater than 200 :{scrsGT200}")
