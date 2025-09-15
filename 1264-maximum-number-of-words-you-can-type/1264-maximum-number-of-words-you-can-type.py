class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        counter = 0
        words = text.split()
        #word ko check krna hai brokenLetters me, Letters ko nhi 

        if len(words) == 0:
            return counter
        if len(brokenLetters) == 0:
            counter = len(words)
            return counter
        

        broken = set(brokenLetters)  


        for w in words:  

            if not any(ch in broken for ch in w):  
                counter += 1  

        return counter
