# 260 - Dado um array inteiro nums, no qual exatamente dois elementos aparecem apenas uma vez e todos os outros elementos aparecem exatamente duas vezes. Encontre os dois elementos que aparecem apenas uma vez. Você pode retornar a resposta em qualquer ordem .

# Você deve escrever um algoritmo que execute em complexidade de tempo de execução linear e use apenas espaço extra constante.

#link do submit: https://leetcode.com/problems/single-number-iii/submissions/888773555/

class Solution:
    def singleNumber(nums: list[int]) -> list[int]:
        nums.sort()
        nova_lista=[]
        numero_sem_par=0
        while(numero_sem_par<=len(nums)-2):
            if nums[numero_sem_par]!=nums[numero_sem_par+1]:
                nova_lista.append(nums[numero_sem_par])
            else:
                numero_sem_par+=1
            numero_sem_par+=1
        if nums[len(nums)-2]!=nums[len(nums)-1]:
            nova_lista.append(nums[len(nums)-1])
        return nova_lista

# teste
nums = [1,2,1,3,2,5]
print(Solution.singleNumber(nums))