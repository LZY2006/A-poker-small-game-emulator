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

def main():
        global desktop, one, another, index, cards
        while True:
            try:
            
                x = one.pop(0)
                # print("x=", dCardsToWords[x], end=" ")
                while step(x, "one"):
                    x = one.pop(0)
                    # print("x=", dCardsToWords[x], end=" ")

                y = another.pop(0)
                # print("y=", dCardsToWords[y], end=" ")
                while step(y, "another"):
                    y = another.pop(0)
                    # print("y=", dCardsToWords[y], end=" ")

                # print(desktop, "", len(one), "", len(another))
                index += 1
            except IndexError:
                break
            if index > 1000:
                break
        if another == []:
            # one won
            return [1, index]
        elif one == []:
            # another won
            return [2, index]
        else:
            # no one won
            return [0, index]

cards = [1,2,3,4,5,6,7,8,9,10,11,12,13] * 4 + [14,15]

index = 0

random.seed(time.time())
random.shuffle(cards)

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
        cards = [1,2,3,4,5,6,7,8,9,10,11,12,13] * 4 + [14,15]
print("one=", one)
print("another=", another)

one_copy = one[:]
another_copy = another[:]

total_steps = 0
total_games = 0
total_one_wins = 0
total_another_wins = 0

while True:

    one = one_copy[:]
    another = another_copy[:]
    index = 0
    random.shuffle(another)
    desktop = []

    stat, n_steps = main()

    total_steps += n_steps

    if stat == 0:
        total_one_wins += 1
        total_another_wins += 1

    elif stat == 1:
        total_one_wins += 1

    elif stat == 2:
        total_another_wins += 1
    
    total_games += 1

    if random.randint(1, 10) == 1:
        print("我方胜率：", total_one_wins / (total_games) * 100, " 平均对局长度：%.2f" %( total_steps / total_games ), " 计算量：", total_steps, end="\r")