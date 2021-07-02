class Solution:

    @staticmethod
    def is_valid(s: str) -> bool:
        stack = []
        for p in s:
            if p in ('(', '{', '['):
                stack.append(p)
            elif not stack or abs(ord(stack.pop()) - ord(p)) > 2:
                return False
        return not bool(stack)


assert Solution.is_valid(s="()") == True
assert Solution.is_valid(s="()[]{}") == True
assert Solution.is_valid(s="(]") == False
assert Solution.is_valid(s="([)]") == False
assert Solution.is_valid(s="{[]}") == True
