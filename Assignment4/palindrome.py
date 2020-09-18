
# Input Parameter: a string x
# Return Value: True if x is a palindrome, False otherwise
def palindrome(x):
    count = -1
    reversevalue = ""   #비교하는 대상이 string 이므로 ""

    for i in x:
        reversevalue = reversevalue+x[count]     #x의 값을 거꾸로 샘 count 가 -1이므로
        count=count-1 #값을 거꾸로 계속 새야되므로 -1씩 계속 빼줌  ex) -1,-2,-3
    Final = x == reversevalue #x는 원래 문자이고 output은 거꾸로 샜으므로 둘이 같으면 true 아니면 false의 값이 나옴
    return Final
        
    
print(palindrome("aba"))
print(palindrome("a"))
print(palindrome("abba"))
print(palindrome("amanaplanacanalpanama"))
print(palindrome("abca"))
print(palindrome("ac"))
print(palindrome("adabbba"))
print(palindrome("amandaplanacanalpanama"))