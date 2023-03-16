class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
         mx =-1
         lst=[]
         for i in range (len (arr) -1 , 0, -1):
              if arr[ i ] > mx:
                   mx = arr[i]
              arr[i] = mx
         arr.remove(arr[0])
         arr.append(-1)
         return(arr)
