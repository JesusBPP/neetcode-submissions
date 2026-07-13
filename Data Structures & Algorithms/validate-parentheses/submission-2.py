class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if(i == '(' or i == '{' or i == '['):
                stack.append(i)
            elif(stack == []) and (i == ')' or i == ']' or i == '}'):
                return False
            elif(i == ')') and ('(' != stack.pop()):
                return False
            elif(i == ']') and ('[' != stack.pop()):
                return False
            elif(i == '}') and ('{' != stack.pop()):
                return False
        if stack == []:
            return True
        else:
            return False
            