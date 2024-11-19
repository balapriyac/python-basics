def linear_search(nums,target):
  for num in nums:
    if num == target:
      return True
  return False


nums = [14,21,27,30,36,2,5,7,11]
target = 27

print(linear_search(nums,target))
# Output: True

target = 100
print(linear_search(nums,target))
# Output: False
