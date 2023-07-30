class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # are we in left sorted part?
            if nums[left] <= nums[mid]:
                if (target > nums[mid]) or (target < nums[left]):
                    # search right portion
                    left = mid + 1
                else:
                    # search left portion
                    right = mid - 1
            else:
                # if we are in right sorted part
                if (target < nums[mid]) or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1