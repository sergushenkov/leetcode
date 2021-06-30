from typing import List


class Solution:

    @staticmethod
    # 40 ms   14.1 MB
    def romanToInt(s: str) -> int:
        nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        last = 1
        for roman in s[::-1]:
            if nums[roman] < last:
                result -= nums[roman]
            else:
                result += nums[roman]
                last = nums[roman]
        return result


assert Solution.romanToInt(s="III") == 3
assert Solution.romanToInt(s="IV") == 4
assert Solution.romanToInt(s="IX") == 9
assert Solution.romanToInt(s="LVIII") == 58
assert Solution.romanToInt(s="MCMXCIV") == 1994
