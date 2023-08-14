nums = [9, 5, 8, 1, 2]
count_perm = 0
while True:
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            count_perm += 1
            nums[i], nums[i+1] = nums[i+1], nums[i]
    if not count_perm:
        break
    count_perm = 0
print(nums)
