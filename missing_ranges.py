#input : [1,2,3,4,10,11,12,22,24,50]
#expected output : ['5->9', '13->21', '23->23', '25->49']


class Missing_ranges:
    def __init__(self):
        self.missing = []

    def find_missing(self,nums):
        for i in range(len(nums)-1):
            if (nums[i]+1) != nums[i+1]:
                self.missing.append (str(nums[i]+1) + '->' + str(nums[i+1]-1))
        return self.missing

x = Missing_ranges()
print (x.find_missing([1,2,3,4,10,11,12,22,24,50]))
