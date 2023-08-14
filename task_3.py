nums = [7, 1, 3, 2, 8]
for i in range(len(nums)):
    for j in range(i):
        if nums[i] < nums[j]:
            item = nums.pop(i)
            nums.insert(j, item)
print(nums)
