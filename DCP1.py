#Finding the pair of number whoose sum is k
#we are passing value which must be sum of the numbers
#the numbers should be present in the list
def DCP1(list,val):
    bool=False
    for i in (range(len(list))):
        for j in (range(i,len(list))):
            result=list[i]+list[j]
            if(result==val):
                bool=True
                break
    return bool

if DCP1([10,3,5,8],17):
    print("Found")
else:
    print('Not Found')
