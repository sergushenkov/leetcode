class Solution:

    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        i = 0
        chars = {}
        result = 0
        for j, a in enumerate(s):
            if a in chars:
                result = max(result, j - i)
                for b in s[i:chars[a]]:
                    chars.pop(b)
                i = chars[a] + 1
            chars[a] = j
        return max(result, len(s) - i)

    # 56 ms	14.1 MB
    @staticmethod
    def length_of_longest_substring_2(s: str) -> int:
        if len(s) <= 1:
            return len(s)
        i = j = 0
        cnt = result = 1
        chars = {s[0]}
        while j < len(s) - 1:
            j += 1
            if s[j] not in chars:
                chars.add(s[j])
                cnt += 1
            else:
                if cnt > result:
                    result = cnt
                while s[i] != s[j]:
                    chars.remove(s[i])
                    i += 1
                i += 1
                cnt = j - i + 1
        if cnt > result:
            return cnt
        return result

    @staticmethod
    def length_of_longest_substring_fast(s: str) -> int:
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i - start)
                start = max(start, dic[ch] + 1)
            dic[ch] = i
        return max(res, len(s) - start)


assert Solution.length_of_longest_substring(s="abcabcbb") == 3
assert Solution.length_of_longest_substring(s="bbbbb") == 1
assert Solution.length_of_longest_substring(s="pwwkew") == 3
assert Solution.length_of_longest_substring(s="") == 0
assert Solution.length_of_longest_substring(s="au") == 2
assert Solution.length_of_longest_substring(s="aabbccddeeabcfdeaabbccddee") == 6

assert Solution.length_of_longest_substring_2(s="abcabcbb") == 3
assert Solution.length_of_longest_substring_2(s="bbbbb") == 1
assert Solution.length_of_longest_substring_2(s="pwwkew") == 3
assert Solution.length_of_longest_substring_2(s="") == 0
assert Solution.length_of_longest_substring_2(s="au") == 2
assert Solution.length_of_longest_substring_2(s="aabbccddeeabcfdeaabbccddee") == 6

assert Solution.length_of_longest_substring_fast(s="abcabcbb") == 3
assert Solution.length_of_longest_substring_fast(s="abbcbabbb") == 3
assert Solution.length_of_longest_substring_fast(s="pwwkew") == 3
assert Solution.length_of_longest_substring_fast(s="") == 0
assert Solution.length_of_longest_substring_fast(s="au") == 2
assert Solution.length_of_longest_substring_fast(s="aabbccddeeabcfdeaabbccddee") == 6
