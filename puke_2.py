##import numba as nb
# A 2 3 4 5 6 7 8 9 10 J  Q  K  JOKER JOKER
# 1 2 3 4 5 6 7 8 9 10 11 12 13  14    15
dWordsToCards = {"A":1,
          "2":2,
          "3":3,
          "4":4,
          "5":5,
          "6":6,
          "7":7,
          "8":8,
          "9":9,
          "10":10,
          "J":11,
          "Q":12,
          "K":13,
          "小王":14,
          "大王":15}
dCardsToWords = {}
for i,j in dWordsToCards.items():
    dCardsToWords[j] = i
##print(dCardsToWords)


import random
import time
import sys


##@nb.jit()
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
        else:
        
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
        else:
            return False
    else:
        raise ValueError
        
cards = [1,2,3,4,5,6,7,8,9,10,11,12,13] * 4 + [14,15]

index = 0

random.seed(time.time())
random.shuffle(cards)

#one = cards[:27].copy()
#another = cards[27:].copy()
one = []
another = []

while True:
    try:
        print()
        print("请输入类似这样的信息：")
        print("A 2 3 4 5 6 7 8 9 10 J Q K 小王 大王")
        input_text = input("One:")
        for i in input_text.split(" "):
            one.append(int(dWordsToCards[i]))
        for i in one:
            cards.remove(int(i))
        another = cards[:]
        break
    except Exception as e:
        print("发生了一个错误。", repr(e))
print("one=", one)
print("another=", another)


desktop = []

def main():
    global desktop, one, another, index, cards
    while True:
        try:
        
            x = one.pop(0)
            print("x=", dCardsToWords[x], end=" ")
            while step(x, "one"):
                x = one.pop(0)
                print("x=", dCardsToWords[x], end=" ")

            y = another.pop(0)
            print("y=", dCardsToWords[y], end=" ")
            while step(y, "another"):
                y = another.pop(0)
                print("y=", dCardsToWords[y], end=" ")

            print(desktop, "", len(one), "", len(another))
            index += 1
        except IndexError:
            break
        if index > 1000:
            break
        #1/0
    print()
    print("♂"*20)
    if another == []:
        print(index, "one")
    elif one == []:
        print(index, "another")
    else:
        print("平")
    print("♂"*20)
    input("按回车继续. . .")

if __name__ == "__main__":
    main()
