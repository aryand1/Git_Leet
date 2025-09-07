class Solution:
    def checkRecord(self, s: str) -> bool:
        absent, late=0,0
        for i in range(len(s)):
            if s[i]== 'A':
                absent+=1
            if s[i:i+3]=='LLL':
                late+=1
        # print(f"Absent: {absent} and Late: {late}")
        if absent<2 and late<1:
            return True
        else: 
            return False
   