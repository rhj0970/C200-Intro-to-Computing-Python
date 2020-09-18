for j in range(1,11,1):
    print(j*"*")

for k in range(9,0,-1):
    print(k*"*")
    
print()


stack = 1
start = 0
for w in range(1,9,1):    #9줄반복하는거
    start = start + stack    #k 실질적으로 쌓아주는 역할
    print(start*"*")    
    stack = stack+1     #스택에 계속 1을 더해주어야 k에서 별1개 만들고 여기서 1+1해서 2개 만든뒤 start는 1이니까 1+2는3개 따라서 홀수단위로 증가함
                        #스택을 1개씩 증가시켜주는 역할
for i in range(1,9,1):
    stack = stack-1    #스택이 위의 식부터 쌓아졋으므로 9부터 시작함 즉 8부터 시작 거꾸로  (스택의 고유 value =1이 밖에 있으므로 reset이 안됨!!
    start = start-stack     #-1로 가니까 거꾸로 시작함 즉 8번째줄부터 시작 여기는 홀수단위로빼줌 거꾸로 -1,-3,-5......
    
    print(start*"*")





a=1
for m in range (21,0,-2):
    print(a*" "+m*"*")    #a의 역할은 m이 *의 값을 내면 그걸 왼쪽에서 2개씩 밀어줌 (2개씩 밀어주는 이유 = m도 -2씩 값을 내므로 정삼각형을 만들기 위함#
    a=a+1
