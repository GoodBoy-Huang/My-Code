'''给你一个仅由数字6和9组成的正整数num
你最多只能翻转一位数字,将6变成9,或者把9变成6。
请返回你可以得到的最大数字'''

class Solution():
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(str(num).replace("6", "9", 1))

num = Solution()
num_max = num.maximum69Number(9669)
print(num_max)
#数字有9669，9969这种由6和9组成的数字
