#TC: O(n) 
#SC:O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        res=[]
        for word in strs:
            key = self.hashcode(word) #key is the hashcode of that string
            if key not in h: 
                h[key] = [word] #if the word is not in hashmap, insert it
            else:
                h[key].append(word) #else append the word in the resultant array
        
        
        
        
        for k,v in h.items():
            res.append(v)
            
        return res #result has the values
        
        
        
    def hashcode(self,s):  #function to create a hashcode for every anagramic string
        c = 0
        for i in s: 
            c += ord(i) ** 5
        return c