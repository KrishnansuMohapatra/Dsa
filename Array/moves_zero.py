def moves_zeros(arr):
    pos=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[pos],arr[i]=arr[i],arr[pos]
            pos+=1
    return arr
input_arr=[2,0,7,8,0,4,0]
print(moves_zeros(input_arr))
    
