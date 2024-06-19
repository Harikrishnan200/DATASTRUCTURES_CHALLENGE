class Solution:
    def targetElementsToRight(self,list:list[int],target:int) ->list[int]:
        left = 0
        right = len(list)-1
        while left<=right:
            if list[left] != target:
                left +=1
            elif list[right] == target:
                right -= 1
            else:
                list[left],list[right] = list[right],list[left]
                left += 1
                right -=1
        return list
print(Solution().targetElementsToRight([6,1,6,3,6,5,7,6,6],6))


