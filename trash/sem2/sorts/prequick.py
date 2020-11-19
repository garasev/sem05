def quick(nums,fst,lst):
    if fst<=lst:
        i,j=fst,lst
        pivot=nums[(i+j)//2]
        while i<=j:
            while nums[i]<pivot:
                i+=1
            while nums[j]>pivot:
                j-=1
            if i<=j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        quick(nums,i,lst)
        quick(nums,fst,j)
        if fst==0 and lst==len(nums)-1:
            return nums
a=[5,2,7,4,0,9,8,6]
quick(a,0,len(a)-1)
print(a)

