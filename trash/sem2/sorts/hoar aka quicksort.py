from random import *
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = nums[len(nums)//2]
       s_nums = []
       m_nums = []
       e_nums = []
       print(q)
       for n in nums:
           print(n)
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       print(s_nums,m_nums,e_nums)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)
nums=[32,95,16,82,24,66,35,19,75,54,40,43,93]
print(quicksort(nums))