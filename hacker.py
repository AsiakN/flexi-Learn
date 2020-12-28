M = int(input())
x = input().split()
N = int(input())
y = input().split()

new_list = list(map(int, x))
set_list = set(new_list)

my_list = list(map(int,y))
set_list2 = set(my_list)

symmetry = set_list.symmetric_difference(set_list2)
syn = sorted(symmetry)
for d in syn:
    print(d)
