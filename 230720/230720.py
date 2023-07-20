import sys
prime = []
check = [False]*1000001
#에라토스테네스의 체

for i in range(2,1000001):
    if check[i]==False:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            check[j]=True

T = int(input())

for _ in range(T):
    count = 0
    N = input(int())
    for i in prime:
        if i>=N:
            break
    if not check(N-i) and i<=N-1:
        count +=1
    print(count)

############################################
# 최대공약수
def euclid(num1, num2): #num1이 더 커야함
    if (num2==0):
        return num1
    return euclid(num2, num1%num2)

# 최소공배수
def get_lcm(num1, num2):
    return num1*num2 / euclid(num1,num2)

