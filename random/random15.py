import heapq

nums = [1,2,400,3]
nums.insert(1,100)
nums.remove(100)
print(100 in nums)
print(nums)

data = [1,1,32,654,654,312,3,5,1,3,85,54,9,55,12,5,12]
data = sorted(data)
print(data)

heapq.heapify(data)

