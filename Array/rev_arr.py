def rev_arr(arr):
    l=0
    r=len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr

def test_rev_arr():
    assert rev_arr([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert rev_arr([10, 20, 30]) == [30, 20, 10]
    assert rev_arr([1]) == [1]
    assert rev_arr([]) == []
    assert rev_arr([-1, -2, -3]) == [-3, -2, -1]
    print("All test cases for rev_arr passed!")

if __name__ == "__main__":
    test_rev_arr()
    # To run with manual input, uncomment below:
    # input_arr=list(map(int,input().split()))
    # print( rev_arr(input_arr))