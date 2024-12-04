from re import finditer


with open("C:\\Users\\micvi\\OneDrive\\Desktop\\pythonworks\\fundamentals\\regular expression\\refile\\hashtag.txt") as f:

   
    for line in f:

     
        new = line.rstrip("\n")

       
        pattern = "#\w+"

        
        matcher = finditer(pattern, new)

        
        for obj in matcher:
            print(obj.group())
