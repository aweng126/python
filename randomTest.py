# -*- coding: UTF-8 -*-
import random
if __name__ == '__main__':
    print(random.randint(1,10)) # 产生 1 到 10 之间的一个整数型随机数
    print(random.random())      # 产生 0 到 1 之间的随机浮点数
    print(random.uniform(1,10)) # 产生 1 到 10 之间的随机浮点数，区间可以不是整数
    print(random.choice('tomorrow')) #从序列中随机选取一个元素
    print(random.randrange(1,100,2)) # 生成从1到100的间隔为2的随机整数

    a = [1,3,5,7,9]
    random.shuffle(a)
    print(a)