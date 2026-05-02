class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(' ', '')

        clean_text = "".join(char for char in s if char.isalnum()).lower()

        print(clean_text)
        print(clean_text[::-1])

        return clean_text == clean_text[::-1]


sol = Solution()

print(sol.isPalindrome("Was it a car or a cat I saw?"))