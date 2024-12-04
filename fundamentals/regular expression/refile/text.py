#from re import finditer

#f=open("C:\\Users\\micvi\\OneDrive\\Desktop\\pythonworks\\fundamentals\\regular expression\\refile\\text.txt")

#for line in f:

  #  new=line.rstrip("\n")

 #   pattern="(https|http)?://[\W\S]+"

 #   matcher=finditer(pattern,new)

 #   for obj in matcher:

 #       print(obj.group())


from re import findall

f=open("C:\\Users\\micvi\\OneDrive\\Desktop\\pythonworks\\fundamentals\\regular expression\\refile\\text.txt")

content=f.read()

pattern="https?://[\w\s./]+"

matcher=findall(pattern,content)

for url in matcher:

    print(url)