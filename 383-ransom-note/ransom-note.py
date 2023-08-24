class Solution:
    # return true if ransomNote can be constructed using magazine's letters
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h = {}
        for c in magazine:
            h[c] = h.get(c, 0) + 1

        for c in ransomNote:
            if c not in magazine:
                return False
            h[c] -= 1
            if h[c] < 0:
                return False



        return True
