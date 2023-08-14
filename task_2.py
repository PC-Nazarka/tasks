nums = [1, 2, 9, 5, 7, 8]
max_item = float("-inf")
max_item_index = 0
position = len(nums) - 1
while position > 0:
    for i in range(position+1):
        if nums[i] > max_item:
            max_item = nums[i]
            max_item_index = i
    nums[max_item_index], nums[position] = nums[position], nums[max_item_index]
    max_item = float("-inf")
    max_item_index = 0
    position -= 1
print(nums)
