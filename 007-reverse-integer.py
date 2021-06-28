class Solution:

    # 28 ms	14.1 MB
    @staticmethod
    def reverse(x: int) -> int:
        if x < 0:
            tgt = -int(str(-x)[::-1])
        else:
            tgt = int(str(x)[::-1])
        if not (-2 ** 31 <= tgt <= 2 ** 31 - 1):
            tgt = 0
        return tgt

    @staticmethod
    # 28 ms	14.2 MB
    # O(lg x)
    def reverse_no_str(x: int) -> int:
        sign = 1
        if x < 0:
            x = -x
            sign = -1
        tgt = 0
        while x > 0:
            digit = x % 10
            tgt = tgt * 10 + digit
            x //= 10
        tgt *= sign
        if not (-2 ** 31 <= tgt <= 2 ** 31 - 1):
            tgt = 0
        return tgt

    # minimalism
    # 36 ms	14.2 MB
    @staticmethod
    def reverse_mini(x: int) -> int:
        sign = [1, -1][x < 0]
        tgt = sign * int(str(abs(x))[::-1])
        return tgt if -2 ** 31 <= tgt < 2 ** 31 else 0


assert Solution.reverse(x=123) == 321
assert Solution.reverse(x=-123) == -321
assert Solution.reverse(x=120) == 21
assert Solution.reverse(x=0) == 0

assert Solution.reverse_no_str(x=123) == 321
assert Solution.reverse_no_str(x=-123) == -321
assert Solution.reverse_no_str(x=120) == 21
assert Solution.reverse_no_str(x=0) == 0

assert Solution.reverse_mini(x=123) == 321
assert Solution.reverse_mini(x=-123) == -321
assert Solution.reverse_mini(x=120) == 21
assert Solution.reverse_mini(x=0) == 0