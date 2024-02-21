import math
import time

nums = list(range(1,20000))
for i in nums:
    root_cube = round(i ** (1/3),5)
    if root_cube.is_integer():
        print(f'This number is {i} and has root cube of {root_cube}')
        time.sleep(1)

print(64 ** (1/3))