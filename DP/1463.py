# 1로 만들기
x = int(input())
a = [0, 0, 1, 1]
for i in range(4,x+1):
    l = []
    if i % 3 == 0:
        l.append(a[i//3]+1)
    if i % 2 == 0:
        l.append(a[i//2]+1)
    l.append(a[i-1]+1)
    a.append(min(l))

print(a[x])
