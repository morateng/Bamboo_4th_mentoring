print("구구단 몇 단을 계산할까?")
n = int(input())
print("구구단 {0}단을 계산한다".format(n))
for i in range(1, 10):
    print(n, " x ", i, " = ", n*i)
