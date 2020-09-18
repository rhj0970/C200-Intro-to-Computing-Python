

def dollars(x):
   x=x*100
   remainderq = x%25
   q=(x//25)
   d=(remainderq//10)
   remainderd = remainderq%10
   n=(remainderd%10//5)
   remaindern = remainderd%5
   p= (remaindern//1)
   
   return q,d,n,p




print(dollars(2.24))
print(dollars(1.19))
print(dollars(4.16))