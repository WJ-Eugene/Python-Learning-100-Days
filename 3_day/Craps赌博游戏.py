"""
Craps 赌博游戏
游戏规则： 玩家掷两个骰子，如果第一次点数和为 7 或 11,则玩家胜;如果点数和为2、3 或 12,则玩家输庄家胜。
若和为其他点数，则记录第一次的点数和，然后玩家继续掷骰子，若和第一次点数的和相同，玩家赢;若和为7,则庄家赢。
"""

import random
x = random.randint(1,7)
y = random.randint(1,7)
one = x + y
print(one)
if (one == 7) or (one == 11):
    print('Player WIN')
elif (one == 2) or (one == 3) or (one == 12):
    print('Boss WIN')
else:
    while True:
        a = random.randint(1,7)
        b = random.randint(1,7)
        if a + b == one:
            print(a + b)
            print('Player WIN')
            break
        elif a + b == 7:
            print(a + b)
            print('Boss WIN')
            break
 