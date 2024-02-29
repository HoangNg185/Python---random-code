def collatz(num:int,n:int)->int:
    for i in range(n):

        if num%2==0:
            num //=2
        else:
            num = num * 3 + 1
        print(num, end=' ')
    return num
collatz(27,100)
print()
def collatz_return_n(num:int)->int:
    n=0
    while num!=1:
        if num%2==0:
            num//=2
        else:
            num=num*3+1
        n+=1
    return n
print(collatz_return_n(256))



