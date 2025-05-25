class Solution:
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        counter=0
        stack =[]
        my_dict = {"(":")","[":"]","{":"}"}
        if len(s)==0:
            counter=1 #<- handles empty string, no comparison made
        elif len(s)==1:
            counter=0
        else:
            for i in range (len(s)): #<- handles the comparison for the entire length of string by pushing the opening item to the stack and comparing the closing item on pop
                if s[i] in ( "(","{","["):
                    stack.append(s[i])
                if s[i] in (")","}","]"):
                    if len(stack)==0:
                        counter=0
                        break
                    close = stack.pop()
                    if s[i]==my_dict[close]:
                        counter=1
                    else: 
                        counter=0
                        break
            if len(stack)!=0: #<- handles only unfinshed parenthesis
                counter=0
        if counter==1:
            return True
        else: return False