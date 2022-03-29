from random import uniform
nums = [round(uniform(0, 1000), 3) for _ in range(100)]

# Sort nums using only the fractional portion of each number.
# Example: 30.12 is bigger than 100.01

def sort_fractional(nums):
    nums = map(str, nums)
    for i, num in enumerate(nums):
        index = num.find('.')
        nums[i] = num[index+1:]
    return sorted(nums)

print sort_fractional(nums)
