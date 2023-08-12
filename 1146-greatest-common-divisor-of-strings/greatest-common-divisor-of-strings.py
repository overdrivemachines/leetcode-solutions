class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""

        if len(str1) > len(str2):
            temp = str1
            str1 = str2
            str2 = temp

        # print("str1: ", str1, "length: ", len(str1))
        # print("str2: ", str2, "length: ", len(str2))
        gcd = math.gcd(len(str1), len(str2))
        # print("gcd:", gcd)

        for i in range(gcd):
            # print("prefix:", str1[0 : i + 1], end=" ")
            if str1[0 : i + 1] == str2[0 : i + 1]:
                result = str1[0 : i + 1]
                # print("present")
            # else:
            #     print("absent")

        # ensure str1's remaining chars match the result
        if gcd < len(str1):
            # print("str1: ", str1, "length:", len(str1))
            for i in range(gcd, len(str1), gcd):
                if (str1[i : i + gcd]) != result:
                    return ""

        # ensure str2's remaining chars match the result
        if gcd < len(str2):
            # print("str2:", str2, "length:", len(str2))
            for i in range(gcd, len(str2), gcd):
                if (str2[i : i + gcd]) != result:
                    return ""

        return result