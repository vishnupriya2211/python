f=open("C:\\Users\\micvi\\OneDrive\\Desktop\\pythonworks\\fundamentals\\looping\\nestedloop\\function\\string\\collection\\dictionary\\nested collection\\database\\sen.txt","r")

words=[]

for i in f:
    
    i=i.rstrip("\n")

    all_words=i.split ( " ")

    for w in all_words:
        words.append(w)
        words_count={w:words.count(w) for w in words}
        nested_word_count=[[v,k] for k,v in words_count.items()]

print(sorted(nested_word_count,reverse=True))