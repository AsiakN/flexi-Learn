n = map(int, input().split())
arr = list(map(int, input().split()))
A = map(int, input().split())
B = map(int, input().split())
arr1 = set(arr)
set_A = set(A)
set_B = set(B)

happiness = 0
for i in arr1:
    if i in set_A:
        happiness += 1
    elif i in set_B:
        happiness -= 1
    else:
        happiness = happiness
print(happiness)
