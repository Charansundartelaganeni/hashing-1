class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):return False
    
        hashMapS = {} #open an S hashmap
        hashMapT = {} #open a T hashmap
        for i in range(0, len(s)):
        
            hashMapS[s[i]] =  i #assign the index as value for the characters in the string as keys
            
       
        for j in range(0, len(t)):
        
            hashMapT[t[j]] = j #assign the index as value for the characters in the string as keys
            

        if list(hashMapT.values()) == list(hashMapS.values()): #if the values of both the hashmaps are equal, then the given strings are isomorphic
        
            return True
        
        return False