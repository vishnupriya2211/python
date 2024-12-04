word=["hello","hai","hello","this","is","this","is","hello"]

word_count={ch:word.count(ch) for ch in word}

print(word_count)

recur=[k for k,v in word.items() if v>1]


print(recur)

non_recur=[k for k,v in word.items() if v==1]

print(non_recur)

