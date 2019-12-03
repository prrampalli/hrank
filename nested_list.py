# Reference - https://github.com/vinsonlee/hackerrank/blob/master/python/nested-list/nested-list.py

N = int(input())

lst = list()
for i in range(N):
    lst.append([input(), float(input())])

arr = set([lst[x][1] for x in range(N)])
arr = list(arr)
arr.sort()

lst = [x[0] for x in lst if x[1] == arr[1]]
lst.sort()

for i in lst:
    print(i)
