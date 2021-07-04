from typing import List


class Solution:

    # 28 ms	14.5 MB
    @staticmethod
    def longest_common_prefix(strs: List[str]) -> str:
        result = ""
        i = 0
        char = set()
        while 1:
            for s in strs:
                try:
                    if not char:
                        char.add(s[i])
                    elif s[i] not in char:
                        return result
                except:
                    return result
            result += char.pop()
            i += 1

    # 36 ms	14.2 MB
    @staticmethod
    def longest_common_prefix_2(strs: List[str]) -> str:
        for i, s in enumerate(strs):
            if i == 0:
                result = s
                continue
            for j in range(min(len(result), len(s))):
                if result[j] != s[j]:
                    result = result[:j]
                    break
            result = result[:j]
        return result


assert Solution.longest_common_prefix(strs=["flower", "flow", "flight"]) == "fl"
assert Solution.longest_common_prefix(["dog", "racecar", "car"]) == ""

assert Solution.longest_common_prefix_2(strs=["flower", "flow", "flight"]) == "fl"
assert Solution.longest_common_prefix_2(["dog", "racecar", "car"]) == ""
