def max_array(arr):
    if not arr:
        return None

    max_arr=arr[0]
    for i in arr:
        if i> max_arr:
            max_arr=i
    return max_arr
input_arr=list(map(int,input().split()))
print(max_array(input_arr))