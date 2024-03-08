def middleElementOfArray(arr):
    low=0
    high=len(arr)-1
    mid=(low+high)//2
    return arr[mid]
print(middleElementOfArray(arr))