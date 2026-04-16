def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
input_arr=list(map(int,input().split()))
print(is_sorted(input_arr))











