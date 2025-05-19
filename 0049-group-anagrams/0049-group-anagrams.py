from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_anagrams=defaultdict(list)
        result=[]
        for s in strs:
            sorted_s = tuple(sorted(s))
            map_anagrams[sorted_s].append(s)

        for value in map_anagrams.values():    
            result.append(value)
        return result

# so ismey ho kya rha hai phley loop me hrr iteration me ek nayi key bann rhi hai sort hokar 
#  jaisey eat ka aet fir tea ka same aet bann rha hai or jaisey hi key bann rhi hai uskey liye 
# str ki original element daal dena hai jaisey harr element ki sorted version key bann gya or unsorted version uska values, sorted version same rahega agr anagram hai to values append hoti jaengi nhi to next pe move ho jaega