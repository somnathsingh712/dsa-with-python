def binarySearch_iterative(data,target):
    low=0
    high=len(data-1)
    while low<=high:
        mid=(low+high)//2
        if target==data[mid]:
            return True
        elif target<data[mid]:
            high=mid-1
        else:
            low=mid+1

    return False



def insertion_sort(a):
    for i in range(1,len(a)):
        curr=a[i]
        j=i
        while j>0 and a[j-1]>curr:
            a[j]=a[j-1]
            j-=1
            a[j]=curr
            
