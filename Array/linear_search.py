def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return True
    return False
print(linear_search([1,2,3,5,4],4))
print(linear_search([1,2,3,5,4],9))
