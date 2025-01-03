# randomly swapping variable without using forth variable
var = ['apple', 'next', 'green']
var[2], var[0], var[1] = var[0], var[1], var[2]
print(var)
