if __name__ == '__main__':
    n = int(input())
    secondMax = 0
    if 2 <= n <= 10:
        arr = list(map(int, input().split()))
        arr.sort()
        high = arr[0]
        secondMax = high
        if n != len(arr):
            exit(0)
        for i in range(0, n):
            if arr[i] not in range(-101, 101):
                exit(0)
            if high < arr[i]:
                secondMax = high
                high = arr[i]
        print(secondMax)



'''
# Other way of doing it is to write another function
def Remove_dupe(arr):
    final_list = []
    for num in arr:
        if num not in final_list:
            final_list.append(num)
    return final_list[-2]

# or you can use print(Remove(duplicate[-2]))
'''
