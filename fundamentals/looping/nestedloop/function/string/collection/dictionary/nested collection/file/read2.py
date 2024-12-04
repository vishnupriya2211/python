f=open("C:\\Users\\micvi\\OneDrive\\Desktop\\pythonworks\\fundamentals\\looping\\nestedloop\\function\\string\\collection\\dictionary\\nested collection\\database\\fruits.txt","r")

fruits=[]
for l in f:
    fruits.append(l.rstrip("\n"))

print(fruits)
