def F(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

n=int(input("서로다른 n개에서 "))
r=int(input("r개를 뽑아서 일렬로 배열"))

print (F(n)/(F(n-r)*F(r)))
