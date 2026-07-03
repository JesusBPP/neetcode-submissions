class Solution:
    def isPalindrome(self, s: str) -> bool:
        slimpio = ""
        bandera = len(slimpio) - 1
        for i in s:
            if i.isalnum():
                slimpio += i
        slimpio = slimpio.lower()
        for j in slimpio:
            if j != slimpio[bandera]:
                return False
            bandera -= 1
        return True