prime=[]
for num in range(100):
    for increase in range(2,num):
        if num % increase ==0:
            break
    else:
        prime.append(num)
print(prime)

def prime_number(list_nums:list)->list:
    prime=[]
    for num in list_nums:
        for increase in range(2,num):
            if num % increase ==0:
                break
        else:
            prime.append(num)
    return prime


print(prime_number(range(int(input('from')),int(input('to')))))