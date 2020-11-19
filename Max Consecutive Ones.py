# Problem Staement = Given a binary array, find the maximum number of consecutive 1s in this array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ser = 0
        listy = []
        
        for i in range (len(nums)):
            
            if nums[i] == 1 :
                count += 1
                
            elif nums[i] != 1 :  
                count = 0
                
            listy.append(count)
            
            
        return(max(listy))
        

                
