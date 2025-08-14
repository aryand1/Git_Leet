class Solution:
    def largestGoodInteger(self, num: str) -> str:
        first = 0
        comp_value1 = []
        while first <= len(num) - 3:
            second = first + 1
            third  = first + 2
            if num[first] == num[second] == num[third]:
                comp_value1.append(num[first] * 3)
            first += 1
        return max(comp_value1) if comp_value1 else ""
