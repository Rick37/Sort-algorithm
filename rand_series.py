# 随机产生一个长度为N的数列，数列中最大值为Max
import random


def random_series(Max=100, N=10):
    lists = []
    for i in range(0, abs((N))):
        lists.append(random.randint(0, abs(Max)))
    return lists


if __name__ == "__main__":
    a = random_series(15, 39)
    print(a)
