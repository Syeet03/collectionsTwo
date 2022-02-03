from random import randint

kaartSoort = ["harten", "ruiten", "schoppen", "klaveren"]
kaarten    = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas"]
joker      = ["joker", "joker"]
game       = list()
result     = list()

for x in range(0,3):
    for y in range(0,12): game.append(kaartSoort[x] + " " + kaarten[y])
for z in range(0,1):
    game.append(joker[z])
for i in range(0, len(game)):
    result.append(game[randint(0, len(game)-1)])
for e in range(0,7):
    print(result[0])
    result.pop(0)
print(result)