import math
def primetest(num):
    if(num <= 1):
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if(num % i == 0):
            return False
    return True
def InverseFermat(b,n):
    if ((b*pow(b,(n-2))) % n == 1):
        return pow(b,(n-2))
def InverseMulOfDivision(b , n):
    for i in range(1,n):
        if((4*i)%9 == 1):
            return i
    return -1
def checkAnswerLength(number , n):
      if(number < n):
        return number
      else:
        return checkAnswerLength(number%n,n)
a , b , n = input().split()
a = int(a)
b = int(b)
n = int(n)
if (primetest(n)):
    if n % b != 0:
       print(checkAnswerLength(InverseFermat(b,n) , n)*a)
    else:
       print(checkAnswerLength(InverseMulOfDivision(b,n)*a , n))
else:
    print(checkAnswerLength(InverseMulOfDivision(b,n)*a , n))

