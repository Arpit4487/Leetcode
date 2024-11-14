class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums

solution = Solution()
example_nums = [3, 1, 2, 10, 1]
result = solution.runningSum(example_nums)
print("Running sum:", result)