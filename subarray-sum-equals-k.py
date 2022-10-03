#TC:O(n) 
#SC:O(n)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0     #initiate answer as zero
        prefixsum = 0  #initiate the running sum as zero
        d = {0:1}  #initiate a hashmap with a key value pair (0,1) initially, as this will help find the initial sub array

        for i in nums:   #traverse through the given array
            prefixsum += i     #always increment the running sum by the values of the given array
            if prefixsum - k in d:    #if the difference of running sum and K is already there in the hashmap, it means an array that has the sum 'k' is found already, so increment ans and also Increase the value of the corresponding key which is given in the else statement given below 
                
                ans += d[prefixsum - k]  

            if prefixsum not in d:    #if the prefixsum is is not in the hashmap, initialize the value as '1'for the corresponding key or else increase the value of the existing key.
                d[prefixsum] = 1
            else:
                d[prefixsum] += 1