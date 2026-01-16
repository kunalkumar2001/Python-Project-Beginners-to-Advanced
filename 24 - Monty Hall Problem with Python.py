import random
from random import seed, randint
import numpy

def game(winningdoor, selecteddoor, change = False):
    assert winningdoor <3
    assert winningdoor >=0

    removedoor = next(i for i in range(3) if i != selecteddoor and i!= winningdoor)

    if change:
        selecteddoor = next(i for i in range(3) if i != selecteddoor and i!= removedoor)

    return selecteddoor == winningdoor


if __name__ == "__main__":
    playersdoors = numpy.random.randint(0,2, (1000*1000*1,))

    winningsdoors = [d for d in playersdoors if game(1,d)]
    print("Winning Percentage without changing choice: ",len(winningsdoors)/len(playersdoors))

    winningsdoors = [d for d in playersdoors if game(1,d, change=True)]
    print("Winning Percentage with changing choice: ",len(winningsdoors)/len(playersdoors)) 
