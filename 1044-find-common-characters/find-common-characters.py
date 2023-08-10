class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 0:
            return []
        result = {}

        for letter in words[0]:
            result[letter] = result.get(letter, 0) + 1

        # print("Result: ", result)

        for word in words[1:]:
            letters = {}
            for c in word:
                letters[c] = letters.get(c, 0) + 1

            # print("letters: ", letters, end=" ")

            for char, count in result.items():
                result[char] = min(count, letters.get(char, 0))

            # print("result: ", result)

        my_list = []

        for char, count in result.items():
            if count > 0:
                while count > 0:
                    my_list.append(char)
                    count -= 1

        return my_list