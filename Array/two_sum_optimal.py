def two_sum_optimal(arr,target):
    hashmap={}
    for i in range(len(arr)):
        compliment=target-arr[i]
        if compliment in hashmap:
            return [hashmap[compliment],i]
        hashmap[arr[i]]=i
    return []
input_arr=[2,7,8,4,0]
find_tar=9
print(two_sum_optimal(input_arr,find_tar))
