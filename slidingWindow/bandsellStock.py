#--------------------brute force o(n2)-------------------------------#

# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:

#         left = 0

#         max_length = 0

#         for i in range(len(prices)-1):
#             for j in range(i+1, len(prices)):
#                 if prices[i]<prices[j]:
#                     max_length = max(max_length,prices[j]-prices[i])

#         return max_length


#-------------------optimal o(n)----------------------------#

class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        left = 0

        right = 1

        max_length = 0

        while right<len(prices):

            if prices[right]>prices[left]:
                max_length = max(max_length, prices[right]-prices[left])

            else:
                left = right

            right+=1

        return max_length



        