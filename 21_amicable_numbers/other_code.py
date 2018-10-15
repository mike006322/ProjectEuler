ls = {}
ls1 = {}
def sum_divisors(n):
    temp = n
    s = 0
    i = 2
    while i < n:
        n = temp // i
        if temp % i == 0:
            s += (i + n)
        i += 1
    return s + 1


for i in range(1,100001):
    ls[i] = (sum_divisors(i))

x = 0

for i in range(1, 100001):
    q = ls[i]
    if q != i:
        if q in ls:
            if i == ls[q]:
                x += i
            else:
                p = sum_divisors(q)
                if i == p:
                    x += i
                    ls1[i] = x

for _ in range(int(input())):
    print(ls1[int(input())-1])
