#30 june 2026
# attendence got rotated due to a system error find student with the given target value 
# arr=(40,50,10,20,30)
# output=3

def find(lst,target):
    low=0
    high=len(lst)-1

    while low<high:
        mid=low+(high-low)//2
        if lst[mst]==target:
            return mid
        if lst[low]<=lst[mid]:

            if lst[low]<=target<=lst[mid]:
                high=mid
            else:
                low=mid+1
        else:
            if lst[mid]<target<=lst[high]:
                low=mid+1
            else:
                high=mid     
        return -1                  

if __name__ == "__main__":
    lst=[40,50,10,20,30]
    target=70
    ans=find(lst,target)
    print(ans)
