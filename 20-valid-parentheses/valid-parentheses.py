class Solution(object):
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == "[":
                stack.append("]")
            elif s[i] == "{":
                stack.append("}")
            elif s[i] == "(":
                stack.append(")")
            else:
                if not stack or stack[-1] != s[i]:
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False

