class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answer = []
        for i, num in enumerate(nums):
            answer.append(nums[nums[i]])
        return answer
        