def avg_arr(arr):
    if not arr:
        return 0
    total=0
    for i in arr:
        total+=i
    return total/len(arr)

def test_avg_arr():
    assert avg_arr([1, 2, 3, 4, 5]) == 3.0
    assert avg_arr([10, 20, 30]) == 20.0
    assert avg_arr([-1, 1]) == 0.0
    assert avg_arr([5]) == 5.0
    assert avg_arr([]) == 0
    print("All test cases for avg_arr passed!")

if __name__ == "__main__":
    test_avg_arr()
    # To run with manual input, uncomment below:
    # input_arr=list(map(int,input().split()))
    # print(avg_arr(input_arr))