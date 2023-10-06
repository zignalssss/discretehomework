#BigO = O(2^n)
def TilingWalkway(n):
    if(n == 1):
        return 1
    if(n == 2):
        return 2
    elif(n > 2):
        return TilingWalkway(n-1) + TilingWalkway(n-2)
num = int(input())
print(TilingWalkway(num))