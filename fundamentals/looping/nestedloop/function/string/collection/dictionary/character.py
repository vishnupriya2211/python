text="ABBACB"

freq_count={ch:text.count(ch) for ch in text}

print(freq_count)

for k,v in freq_count.items():

    if v==1:
        print(k)
#list comprehension 

non_recur=[ k for k,v in freq_count.items() if v==1]

print(non_recur)