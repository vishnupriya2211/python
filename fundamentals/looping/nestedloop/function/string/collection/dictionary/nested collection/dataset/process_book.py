from json import load

f=open("C:\\Users\\micvi\\OneDrive\\Desktop\\pythonworks\\fundamentals\\looping\\nestedloop\\function\\string\\collection\\dictionary\\nested collection\\dataset\\books.json")

data=load(f)

#for i in data:
#    print(i)

#all_title=[book.get("title") for book in data]

#print(all_title)

#pages_of_book=[i.get("title") for i in data if i.get("pages")< 250]

#print(pages_of_book)

#genre_=[i.get("genre") for i in data]

#print(set(genre_))

#genre_count={genre:genre_.count(genre) for genre in genre_}

#print(genre_count)

#costly=max(data,key=lambda d:d.get("price"))

#print(costly)

author_books=[i.get("author")for i in data ]

#print(author_books)

authors_count={counts:author_books.count(counts) for counts in author_books}

print([k for k,v in authors_count.items() if v>1])