a = [[1, 2, 3], [4, 5, 6]]
# print(a[0])
# print(a[1])
# print(a[1][1])

for row in a:
    for elem in row:
        print(elem, end='   ')
    print()

a[1][1] = 8

print(10*'=')
for row in a:
    for elem in row:
        print(elem, end='   ')
    print()