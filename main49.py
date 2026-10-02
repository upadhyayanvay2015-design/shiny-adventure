class pair:
    def two(self,nums,target):
        lookup={}
        for i,num in enumerate(nums):
            if target-num in lookup:
                return (lookup[target-num],i)
            lookup[num]=i
value=int(input("Enter the sum for which you want to make this search: "))
print("index1=%d,index2=%d"%(pair().two((100,200,300,400,500),value)))
