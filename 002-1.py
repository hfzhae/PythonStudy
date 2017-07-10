import random

number = input("猜猜我心里的数字是几：")

numberInt = int(number)

if isinstance(numberInt, int) == True:
    numberR = random.randint(1,10)
    i = 0

    while numberInt != numberR and i < 3:
        if numberInt == numberR:
            print("对了！")
        else:
            print("错了！应该是：" + str(numberR))
            if numberInt > numberR:
                print("太大了！")
            else:
                print("太小了！")
        i += 1
        number = input("错了！再猜猜我心里的数字是几：")
        numberInt = int(number)

    if i<=3:
        print("对了！")
else:
    print("你应该输入数字的！")

print("游戏结束！")
