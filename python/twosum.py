nums = [2,7,11,15]
target = 9
for i,num in enumerate(nums):
    for i2,num2 in enumerate(nums[i + 1:]):
        if num + num2 == target:
            i2_real = i2 + i + 1
            print([i,i2_real])