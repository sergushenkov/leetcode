class Solution:

    @staticmethod
    # 40 ms   14.1 MB
    def roman_to_int(s: str) -> int:
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

    @staticmethod
    # 44 ms	14.3 MB
    def roman_to_int_2(s: str) -> int:
        nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL', 'XXXX').replace('XC', 'LXXXX') \
            .replace('CD', 'CCCC').replace('CM', 'DCCCC')
        return sum([nums[i] for i in s])

    @staticmethod
    # 44 ms	14.1 MB
    def roman_to_int_minimal(s: str) -> int:
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
            result, last = result - nums[roman] if nums[roman] < last else result + nums[roman], nums[roman]
        return result


assert Solution.roman_to_int(s="III") == 3
assert Solution.roman_to_int(s="IV") == 4
assert Solution.roman_to_int(s="IX") == 9
assert Solution.roman_to_int(s="LVIII") == 58
assert Solution.roman_to_int(s="MCMXCIV") == 1994

assert Solution.roman_to_int_2(s="III") == 3
assert Solution.roman_to_int_2(s="IV") == 4
assert Solution.roman_to_int_2(s="IX") == 9
assert Solution.roman_to_int_2(s="LVIII") == 58
assert Solution.roman_to_int_2(s="MCMXCIV") == 1994

assert Solution.roman_to_int_minimal(s="III") == 3
assert Solution.roman_to_int_minimal(s="IV") == 4
assert Solution.roman_to_int_minimal(s="IX") == 9
assert Solution.roman_to_int_minimal(s="LVIII") == 58
assert Solution.roman_to_int_minimal(s="MCMXCIV") == 1994
