def finalStockPrice(x):
    stack = 0;
    finalPrice = 0;
    
    for i in x[1]:   #2번째 괄호부터 시작
        finalPrice = finalPrice + x[1][stack]   #x[1]에서 stack 한 이유는 x[1]안에도 여러 value가 있으므로 [0],[1]씩 해서 더해주어야함
        stack = stack + 1  #0에서 시작해서 1개씩 더해가면 차례로 더해감 [0]끝나고 [1]......
            
    finalPrice= x[0] + finalPrice   #1번째 괄호를 2번째랑 더함 첫번째 괄호는 어차피 값이 1개이므로 따로 식을 쓰지 않고 바로 더함
    return finalPrice




        
            
stock1 = [10, [1,-.5,2,-1.45]]
stock2 = [2, [.4, -.2,.1,.05,-.23,.03]]
stock3 = [400,[10,-9,9,9,-20,24,-22,100,-24,-23]]


stocks= [stock1, stock2,stock3]

for i in stocks:
    print(finalStockPrice(i))