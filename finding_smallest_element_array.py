def findingSmallestElement(arr):

    min_val=arr[0]
    for num in arr:
        if num< min_val:
            min_val=num
    return min_val
input_arr=list(map(int,input().split()))
print(findingSmallestElement(input_arr))

