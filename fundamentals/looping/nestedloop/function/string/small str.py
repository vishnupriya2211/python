text1="PQRST"

text2="ABC"

smallest_text=text1 if text1 < text2 else text2

largest_text=text1 if text1 > text2 else text2

result=""

for i in range(0,len(smallest_text)):
    result+=text1[i] + text2[i]
balance_text= largest_text[len(smallest_text):]

result+=balance_text

print(result)