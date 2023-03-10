#  164 . Espaço Máximo
#  Dado um array inteiro nums, retorne a diferença máxima entre dois elementos sucessivos em sua forma ordenada . Se a matriz contiver menos de dois elementos, retorne 0.

# Você deve escrever um algoritmo que execute em tempo linear e use espaço extra linear.

#link do submit: https://leetcode.com/problems/maximum-gap/submissions/888772983/
class Solution:
    def maximumGap(nums: list[int]) -> int:
        if len(nums)<2:
            return 0
        if len(nums)==2:
            return abs(nums[0]-nums[1])
        nums.sort()
        lista_de_diferenca_maxima=[]
        for i in range(0,len(nums)-1):
            lista_de_diferenca_maxima.append(nums[i+1]-nums[i])
        return max(lista_de_diferenca_maxima)
 
 # teste
nums = [3,6,9,1]
print(Solution.maximumGap(nums))