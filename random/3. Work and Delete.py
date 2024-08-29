import math


def is_perfect_number_optimized(n):
    if n < 2:
        return False
    sum_divisors = 1  # 1 is always a proper divisor
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:  # modulus ==0
            sum_divisors += i
            corresponding_divisor = n // i  # find floor division
            if corresponding_divisor != i:
                sum_divisors += corresponding_divisor
    return sum_divisors == n


is_perfect_number_optimized(28)
if is_perfect_number_optimized(28) == True:
    print('is perfect')
else:
    print('not')

print(28 // 3)
