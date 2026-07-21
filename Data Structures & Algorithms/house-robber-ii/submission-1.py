class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1 :
            return nums[0]

        def rob_linear(arr) :
            rob1 = 0
            rob2 = 0
            for money in arr :
                temp = max(rob1 + money,rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(
            rob_linear(nums[:-1]),
            rob_linear(nums[1:])
        )        