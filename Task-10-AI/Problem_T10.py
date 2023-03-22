class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
    
        lMax = 0
        rMax = 0
  
        result = 0
        while (left <= right):
            if rMax <= lMax:
                result += max(0, rMax-height[right])
            
                rMax = max(rMax, height[right])
              
                right -= 1
            else:
                result += max(0, lMax-height[left])

                lMax = max(lMax, height[left])
  
                left += 1
        return result