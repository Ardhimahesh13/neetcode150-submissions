class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        sorted_items = sorted(count.keys(),key = lambda x : count[x],reverse = True)
        return sorted_items[:k]


        