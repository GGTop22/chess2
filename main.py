def symbolsToIntCoord(k: str) -> (int, int):
    a = ord(k[0]) - ord('A') + 1
    b = int(k[1])
    return (a, b)


def isKnightJump(p1: (int, int), p2: (int, int)) -> bool:
    return (abs(p1[0] - p2[0]) == 2 and abs(p1[1] - p2[1]) == 1) or (
            abs(p1[0] - p2[0]) == 1 and abs(p1[1] - p2[1]) == 2)


def isBishopJump(p1: (int, int), p2: (int, int)) -> bool:
    return (abs(p1[0] - p2[0])) == (abs(p1[1] - p2[1]))

def isQueenJump(p1: (int, int), p2: (int, int)) -> bool:
    return isBishopJump(p1,p2) or isRookJump(p1,p2)

def isRookJump(p1: (int, int), p2: (int, int)) -> bool:
    return (p1[0] == p2[0]) or (p1[1] == p2[1])


def countMovesKnight(p1):
    move = [2, 1], [2, -1], [1, 2], [-1, 2], [-2, -1], [1, -2], [-1, -2]

    # verhnee pravo /2 vverh,1 vpravo
    # verhnee levo /2 vverh,-1 vpravo
    # praviy verh /1 vverh,2 vpravo
    # praviy niz/-1 vverh,2 vpravo
    # niznie levo/-2 vverh,-1 vpravo
    # niznie pravo/-2 vverh,1 vpravo
    # leviy verh/1 vverh,-2 vpravo
    # leviy niz/-1 vverh,-2 vpravo


def countMovesQueen(p1):
    move = [1], [-1], [2], [-2], [3], [-3], [4], [-4], [5], [-5], [6], [-6], [7], [-7], [8], [-8]


def countMovesRook(p1):
    move = [1], [-1], [2], [-2], [3], [-3], [4], [-4], [5], [-5], [6], [-6], [7], [-7], [8], [-8]


#with open('INPUT.TXT', 'r') as input:
  #  with open('OUTPUT.TXT', 'w') as output:
# output.write((input.readline().strip()))
