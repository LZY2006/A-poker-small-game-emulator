# A 2 3 4 5 6 7 8 9 10 J  Q  K  JOKER JOKER
# 1 2 3 4 5 6 7 8 9 10 11 12 13  14    15
import random
import time



def step(x, _list):
    global desktop, one, another
    desktop.append(x)

    if _list == "one":
    
        if x in desktop[:-1]:

            pos = desktop[:-1].index(x)
            for i in desktop[pos:]:
                one.append(i)
            desktop = desktop[:pos]
            return True
            
        elif (x == 14) or (x == 15):
            for j in desktop:
                one.append(j)
            desktop = []
            return True
        
        return False
    elif _list == "another":
        if x in desktop[:-1]:

            pos = desktop[:-1].index(x)
            for i in desktop[pos:]:
                another.append(i)
            desktop = desktop[:pos]
            return True
            
        elif (x == 14) or (x == 15):
            for j in desktop:
                another.append(j)
            desktop = []
            return True
        
        return False
    else:
        raise ValueError
        
cards = [1,2,3,4,5,6,7,8,9,10,11,12,13] * 4 + [14,15]

random.seed(time.time())
random.shuffle(cards)

one = cards[:27].copy()
another = cards[27:].copy()

desktop = []
# index = 0
result = []




index = 0

random.seed(time.time())
random.shuffle(cards)

one = cards[:27].copy()
another = cards[27:].copy()

desktop = []
#result = []
def main():
    global cards, one, another, desktop, result, index
    cards = [1,2,3,4,5,6,7,8,9,10,11,12,13] * 4 + [14,15]

    random.seed(time.time())
    random.shuffle(cards)

    one = cards[:27].copy()
    another = cards[27:].copy()

    desktop = []
    # index = 0
    result = []




    index = 0

    random.seed(time.time())
    random.shuffle(cards)

    one = cards[:27].copy()
    another = cards[27:].copy()

    desktop = []
    while True:
        try:
        
            x = one.pop(0)

            while step(x, "one"):
                x = one.pop(0)
                
            y = another.pop(0)
            while step(y, "another"):
                y = another.pop(0)
            #print(desktop, x, y)
            index += 1
        except IndexError:
            break
        if index > 1000:
            break

##if another == []:
##    print(index, "one")
##elif one == []:
##    print(index, "another")
##else:
##    print("平")
