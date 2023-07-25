class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        count = dict()
        left, right = 0, 0
        while right < len(s):
            # print(left, "...", right, end=" ")
            # add right to the count dictionary
            count[s[right]] = count.get(s[right], 0) + 1
            # most repeating char count in the window
            max_count = 0
            for c in count.values():
                max_count = max(max_count, c)

            # print(
            #     s[left : right + 1],
            #     count,
            #     "max_count:",
            #     max_count,
            #     "window size:",
            #     right - left + 1,
            #     end=" ",
            # )

            # Check if window is valid
            if (right - left + 1) - max_count <= k:
                result = max(result, right - left + 1)
                right += 1
                # print("valid")

            else:
                # print("invalid")
                count[s[left]] -= 1
                count[s[right]] -= 1
                left += 1

        return result