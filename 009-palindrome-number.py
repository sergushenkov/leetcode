class Solution:

    # 64 ms	14.3 MB
    @staticmethod
    def is_palindrome_3(x: int) -> bool:
        if x < 0:
            return False
        copy_x = x
        reverse = 0
        while copy_x > 0:
            reverse = reverse * 10 + copy_x % 10
            copy_x //= 10
        return x == reverse

    # 48 ms	14.3 MB
    @staticmethod
    def is_palindrome_str(x: int) -> bool:
        if x < 0:
            return False
        return x == int(str(x)[::-1])

    # 76 ms	14.2 MB
    @staticmethod
    def is_palindrome_2(x: int) -> bool:
        if x < 0:
            return False
        b = 1
        while x / b >= 10:
            b *= 10
        while b >= 10:
            if x // b != x % 10:
                return False
            x, b = (x % b) // 10, b / 100
        return True

    # 48 ms	13.9 MB
    @staticmethod
    def is_palindrome_str_2(x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

    # 60 ms	14.2 MB
    @staticmethod
    def is_palindrome(x: int) -> bool:
        if x < 0 or x % 10 == 0:
            return False
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //= 10
        return x == reverse or x == reverse // 10



assert Solution.is_palindrome(x=121) is True
assert Solution.is_palindrome(x=-121) is False
assert Solution.is_palindrome(x=10) is False
assert Solution.is_palindrome(x=-101) is False

assert Solution.is_palindrome_str(x=121) is True
assert Solution.is_palindrome_str(x=-121) is False
assert Solution.is_palindrome_str(x=10) is False
assert Solution.is_palindrome_str(x=-101) is False

assert Solution.is_palindrome_2(x=121) is True
assert Solution.is_palindrome_2(x=-121) is False
assert Solution.is_palindrome_2(x=10) is False
assert Solution.is_palindrome_2(x=-101) is False

assert Solution.is_palindrome_str_2(x=121) is True
assert Solution.is_palindrome_str_2(x=-121) is False
assert Solution.is_palindrome_str_2(x=10) is False
assert Solution.is_palindrome_str_2(x=-101) is False

assert Solution.is_palindrome_3(x=121) is True
assert Solution.is_palindrome_3(x=-121) is False
assert Solution.is_palindrome_3(x=10) is False
assert Solution.is_palindrome_3(x=-101) is False
