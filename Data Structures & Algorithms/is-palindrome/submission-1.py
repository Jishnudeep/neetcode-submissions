import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        print(cleaned_string)
        if cleaned_string == cleaned_string[::-1]:
            return True
        else:
            return False
        