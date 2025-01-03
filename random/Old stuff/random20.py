# what is missing in this array?
nums = [0, 1, 3, 5, 8, 10, 30, 15]

missing = []
start = 0

while start <= max(nums):
    if start not in nums:
        missing.append(start)
    start += 1
print(missing)
