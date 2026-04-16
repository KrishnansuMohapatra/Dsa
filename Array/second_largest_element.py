def second_largest(arr):


    first=float("-inf")
    second=float("-inf")
    for num in arr:
        if num>first:
            second=first
            first=num
        elif num>second and num!=first:
            second=num
    return second if second != float("-inf") else None
input_arr=list(map(int,input().split()))
print(second_largest(input_arr))
