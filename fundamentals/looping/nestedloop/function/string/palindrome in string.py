#text=input("enter the string:")

#reversed_string=text[::-1]

#print("palindorme" if text==reversed_string else "not palindrome")

text="hello"
#01234

length=len(text)-1

reversed_str=""


for i in range(length,-1,-1):

    reversed_str+=text[i]

    print(reversed_str)