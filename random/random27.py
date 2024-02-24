#Remove dupplicate from an array. trick is just create function update current array by indexing.
#Let keep first index as it is, update next index if any different between indexes.
#This is new whole ideaoligy concept, so take ease.

def removeDuplicates(nums):
    if not nums:
        return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return nums[:slow + 1]

resul=removeDuplicates([1,1,2,2,2,2,3,4])
print(resul)