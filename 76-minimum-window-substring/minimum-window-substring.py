class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result_size = len(s) + 1
        result_window_indexes = [0, -1]

        add_right = True

        count_window, count_t = {}, {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        have, need = 0, len(t)
        left, right = 0, 0

        # print(s, t)
        # print("Need:", need)

        # advance left pointer until we see a character present in t
        while (left < len(s)) and s[left] not in count_t:
            left += 1

        if left >= len(s):
            return ""

        right = left

        # print("Left:", left, "Right:", right)

        while (left <= (len(s) - need)) and (right < len(s)):
            # if right pointer does not exist in t, increment right pointer
            while right < len(s) and s[right] not in count_t:
                right += 1

            if right >= len(s):
                break

            # TODO: check if right pointer is in t: if s[right] not in count_t.

            # print("Window:", s[left : right + 1], end=" ")

            if add_right:
                # add right pointer to count_window
                count_window[s[right]] = count_window.get(s[right], 0) + 1
                # increment have counter only if the charecter added to the window is not useless
                if count_window[s[right]] <= count_t[s[right]]:
                    have += 1

            # print(count_window, "have:", have)

            if have == need:
                found_indexes = [left, right]

                window_size = right - left + 1
                # print("Found. Indexes:", found_indexes, "Window Size:", window_size)
                if window_size < result_size:
                    result_size = window_size
                    result_window_indexes = [left, right]
                # print("Smallest Window:", result_window_indexes)
                if window_size == len(t):
                    return s[result_window_indexes[0] : result_window_indexes[1] + 1]

                # remove left pointer from count_window and advance left pointer
                count_window[s[left]] -= 1
                if count_window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
                while (s[left] not in count_t) and (left <= (len(s) - need)):
                    left += 1

                # print(
                #     "New Left:",
                #     left,
                #     "Right:",
                #     right,
                #     "New Window:",
                #     s[left : right + 1],
                #     count_window,
                # )

            add_right = True

            if have != need:
                right += 1
            else:
                add_right = False

        return s[result_window_indexes[0] : result_window_indexes[1] + 1]