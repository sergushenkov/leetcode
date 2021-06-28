from typing import List


class Solution:
    # 48 ms	15.3 MB
    # O(n) - create dict and find pair at the same time!
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        res = dict()
        for i, a in enumerate(nums):
            if (target - a) in res:
                return [res[target - a], i]
            res[a] = i

    # 60 ms	16.2 MB
    # 2*O(n) - create dict and find pair in dict
    @staticmethod
    def two_sum_2(nums: List[int], target: int) -> List[int]:
        nums_d = dict()
        for i, a in enumerate(nums):
            idx = nums_d.get(a, [])
            idx.append(i)
            nums_d[a] = idx
        for a in nums_d:
            if (target - a) in nums_d:
                if 2 * a != target:
                    result = nums_d[a]
                    result.extend(nums_d[target - a])
                    return result
                elif len(nums_d[a]) > 1:
                    return nums_d[a]

    # pattern 2_points needed sorted list
    # 992 ms	15.6 MB
    @staticmethod
    def two_sum_2p(nums: List[int], target: int) -> List[int]:
        res = []
        for i, a in enumerate(nums):
            res.append((a, i))
            res = sorted(res)
        i, j = 0, len(res) - 1
        while i < j:
            if res[i][0] + res[j][0] < target:
                i += 1
            elif res[i][0] + res[j][0] > target:
                j -= 1
            else:
                return [res[i][1], res[j][1]]
        print('not solution')

    # brute force O(n^2)
    # 3776 ms	14.7 MB
    @staticmethod
    def two_sum_bf(nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for j, other_num in enumerate(nums[i + 1:]):
                if num + other_num == target:
                    return [i, j + i + 1]


assert Solution.two_sum(nums=[2, 7, 11, 15], target=9) == [0, 1]
assert Solution.two_sum(nums=[3, 2, 4], target=6) == [1, 2]
assert Solution.two_sum(nums=[3, 3], target=6) == [0, 1]
assert Solution.two_sum(nums=[0, 4, 3, 0], target=0) == [0, 3]

assert Solution.two_sum_2(nums=[2, 7, 11, 15], target=9) == [0, 1]
assert Solution.two_sum_2(nums=[3, 2, 4], target=6) == [1, 2]
assert Solution.two_sum_2(nums=[3, 3], target=6) == [0, 1]
assert Solution.two_sum_2(nums=[0, 4, 3, 0], target=0) == [0, 3]

assert Solution.two_sum_2p(nums=[2, 7, 11, 15], target=9) == [0, 1]
assert Solution.two_sum_2p(nums=[3, 2, 4], target=6) == [1, 2]
assert Solution.two_sum_2p(nums=[3, 3], target=6) == [0, 1]
assert Solution.two_sum_2p(nums=[0, 4, 3, 0], target=0) == [0, 3]

assert Solution.two_sum_bf(nums=[2, 7, 11, 15], target=9) == [0, 1]
assert Solution.two_sum_bf(nums=[3, 2, 4], target=6) == [1, 2]
assert Solution.two_sum_bf(nums=[3, 3], target=6) == [0, 1]
assert Solution.two_sum_bf(nums=[0, 4, 3, 0], target=0) == [0, 3]
