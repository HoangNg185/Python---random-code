# Between these 2 numbers, what are prime numbers? aka: only divided by its self and 1
lower= 90
upper=250

prime=[]
increase=2
for i in range(lower,upper+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        prime.append(i)
print(f'Prime numbers between {lower} and {upper} are: \n{prime}')


