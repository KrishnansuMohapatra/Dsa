def two_sum_brute_force(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return [i,j]
    return []
input_arr=[2,7,8,4,0]
find_tar=9
print(two_sum_brute_force(input_arr,find_tar))
