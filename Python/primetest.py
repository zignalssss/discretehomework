import math
def primetest(num):
    if(num <= 1):
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if(num % i == 0):
            return False
    return True
n = int(input())
if(primetest(n)):
    print("YES")
else:
    print("NO")