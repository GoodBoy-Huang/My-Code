#在闭区间范围内统计奇数数目
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = []
        for x in range(low,high+1):
            if x%2 == 0:
                continue
            else :
                result.append(x)
        return len(result)

low = int(input('please enter low value:'))
high = int(input('please enter high value:'))
count = Solution()
num_odd_count = count.countOdds(low,high)
print("count odds is: ",num_odd_count)
