class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        # count the occurrences of each character
        count = {}
        left = 0
        maxf = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxf = max(maxf, count[s[right]])

            # Check if window is valid
            # When Window size - Count of the most repeating char in the window > k,
            # move the left pointer to the right
            # In other words when the number of characters to be replaced in the window is greater than k,
            # move the left pointer to the right
            # while (right - left + 1 - max(count.values())) > k:
            while (right - left + 1 - maxf) > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
            while (right - left + 1 - max(count.values())) > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
        return result