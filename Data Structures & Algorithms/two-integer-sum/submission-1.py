class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)) :
            remaining = target - nums[i]
            if remaining in d :
                return [d[remaining],i]
            d[nums[i]] = i
        return []

        