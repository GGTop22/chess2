def symbolsToIntCoord(k: str) -> (int, int):
    a = ord(k[0]) - ord('A') + 1
    b = int(k[1])
    return (a, b)


def isKnightJump(p1: (int, int), p2: (int, int)) -> bool:
    return (abs(p1[0] - p2[0]) == 2 and abs(p1[1] - p2[1]) == 1) or (
            abs(p1[0] - p2[0]) == 1 and abs(p1[1] - p2[1]) == 2)


def countMoves(p1):
    move = [2, 1], [2, -1], [1, 2], [-1, 2], [-2, -1], [1, -2], [-1, -2]

    # verhnee pravo /2 vverh,1 vpravo
    # verhnee levo /2 vverh,-1 vpravo
    # praviy verh /1 vverh,2 vpravo
    # praviy niz/-1 vverh,2 vpravo
    # niznie levo/-2 vverh,-1 vpravo
    # niznie pravo/-2 vverh,1 vpravo
    # leviy verh/1 vverh,-2 vpravo
    # leviy niz/-1 vverh,-2 vpravo
