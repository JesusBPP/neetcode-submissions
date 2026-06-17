class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repetido = None
        nums.sort()
        for i in nums:
            if repetido == i:
                return True
            repetido = i
        return False