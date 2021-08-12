from random import randint
logging = False

def log(string):
    if logging: print(string)

def game(switch=False):
    log('INFO | New game started')
    doors = [0, 0, 0]
    
    winningDoor = randint(0, 2)
    doors[winningDoor] = 1
    log('INFO | Winning door: ' + str(winningDoor))

    chosenDoor = randint(0, 2)

    if switch:
        goatDoor = randint(0, 2)
        while goatDoor == chosenDoor or goatDoor == winningDoor:
            goatDoor = randint(0, 2)
        
        temp = chosenDoor
        while chosenDoor == temp or chosenDoor == goatDoor:
            chosenDoor = randint(0, 2)

    if chosenDoor == winningDoor:
        log('RESULT | User won')
        return True
    else:
        log('RESULT | User lost')
        return False

wins = 0
losses = 0

iters = 10000000
for i in range(0, iters):
    if game(switch=False):
        wins = wins + 1
    else:
        losses = losses + 1

print('\n\nRESULTS\n---------')
print('WINS: ' + str(wins))
print('LOSSES: ' + str(losses))

print('Win %: ' + str(wins / iters * 100))