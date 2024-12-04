
read_path = "C:\\Users\\micvi\\OneDrive\\Desktop\\pythonworks\\fundamentals\\looping\\nestedloop\\function\\string\\collection\\dictionary\\nested collection\\database\\words.txt"
write_path = "C:\\Users\\micvi\\OneDrive\\Desktop\\pythonworks\\fundamentals\\looping\\nestedloop\\function\\string\\collection\\dictionary\\nested collection\\database\\palindrome.txt"


f_read=open(read_path, "r")  
f_write=open(write_path, "w") 
    
for line in f_read:
        new = line.rstrip("\n")  
        reversed_word = new[::-1]  
        
        
        if new == reversed_word:
            f_write.write(new + "\n")  
f_read.close()
f_write.close()