class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mini =float(inf)
        ar=[area,1]
        for w in range (1, int(area **0.5)+1):
            l=area/w
            if l==int(l) and l>=w and l-w<mini:
                ar[0]=int(l)
                ar[1]=w
                mini=l-w
        return ar