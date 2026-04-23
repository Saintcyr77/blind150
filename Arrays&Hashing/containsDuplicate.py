class Solution:

    def hasDuplicate(self, nums: list[int]) -> bool:

        s = set()


        for i in nums:

           if i in s:
            return True

           s.add(i)
            

        return False



obj = Solution()

print(obj.hasDuplicate([1, 2, 3, 3]))