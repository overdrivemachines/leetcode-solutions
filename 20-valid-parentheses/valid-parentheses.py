class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif c == ")":
                if not stack:
                    return False
                popped_item = stack.pop()
                if popped_item != "(":
                    return False
            elif c == "]":
                if not stack:
                    return False
                popped_item = stack.pop()
                if popped_item != "[":
                    return False
            elif c == "}":
                if not stack:
                    return False
                popped_item = stack.pop()
                if popped_item != "{":
                    return False
            else:
                "Wrong input"
                return False

        if len(stack) > 0:
            return False
        return True