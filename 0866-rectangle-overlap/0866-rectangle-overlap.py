class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # print(str(rec2[0])+ 'and' + str(rec2[3])) #-> 1and3 for first example
        #logic:
        # Rec1 X1and Y1 should be less than Rec2 X1Y1 and less than X2Y2 of rec1 

        #and 
        #Rec1 X2Y2 should be less than Rec 2 X2y2
        if rec1[2] <= rec2[0]:
                    return False
        elif rec2[2] <= rec1[0]:
                return False
        elif rec1[3] <= rec2[1]:
            return False
        elif rec2[3] <= rec1[1]:
                return False
        return True
