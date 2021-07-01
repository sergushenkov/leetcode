class Solution:

    @staticmethod
    # 56 ms	14.3 MB
    def int_to_roman(num: int) -> str:
        nums = [(1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'),
                (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'),
                (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]
        src = []
        rank = 0
        while num > 0:
            src.append(num % 10 * 10 ** rank)
            num //= 10
            rank += 1
        result = ''
        num = nums.pop()
        while src:
            x = src.pop()
            while x > 0:
                if x >= num[0]:
                    result += num[1]
                    x -= num[0]
                elif x < num[0]:
                    num = nums.pop()
        return result


assert Solution.int_to_roman(num=3) == "III"
assert Solution.int_to_roman(num=4) == "IV"
assert Solution.int_to_roman(num=9) == "IX"
assert Solution.int_to_roman(num=58) == "LVIII"
assert Solution.int_to_roman(num=1994) == "MCMXCIV"
