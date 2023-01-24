# -- coding: utf-8 --
def IsPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("NO")
            return
    print("YES")
n = int(input())
IsPrime(n)