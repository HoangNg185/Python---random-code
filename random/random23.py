#in those numbers, what sum value equal to target value
nums= [2,7,11,15]
target= 22

for i in nums:
    for j in nums:
        if i+j==target:
            print(f'{i} +{j} = {target}')