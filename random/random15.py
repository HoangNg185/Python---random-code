import heapq

nums = [1,2,400,3]
nums.insert(1,100)
nums.remove(100)
print(100 in nums)
print(nums)

data = [50,30,20,15,10,8,16]
heapq.heapify(data)

print('heapified data: ',data)
print(heapq.heappop(data))
print(heapq.heappop(data))
print(heapq.heappop(data))
print(heapq.heappop(data))
print(heapq.heappop(data))
print(heapq.heappop(data))
print(heapq.heappop(data))


