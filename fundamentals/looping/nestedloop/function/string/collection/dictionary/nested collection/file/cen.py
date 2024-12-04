
years = "C:\\Users\\micvi\\OneDrive\\Desktop\\pythonworks\\fundamentals\\looping\\nestedloop\\function\\string\\collection\\dictionary\\nested collection\\database\\ye.txt"
century_year = "C:\\Users\\micvi\\OneDrive\\Desktop\\pythonworks\\fundamentals\\looping\\nestedloop\\function\\string\\collection\\dictionary\\nested collection\\database\\cen.txt"
leap_year = "C:\\Users\\micvi\\OneDrive\\Desktop\\pythonworks\\fundamentals\\looping\\nestedloop\\function\\string\\collection\\dictionary\\nested collection\\database\\leap.txt"


f_year= open(years, "r")
f_century_year=open(century_year, "w") 
f_leap_year=open(leap_year, "w") 


for year in f_year:
        year = int(year)  

        
        if year % 100 == 0:
            f_century_year.write(str(year) + "\n")

    
        if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
            f_leap_year.write(str(year) + "\n")

f_year.close()

f_century_year.close()

f_leap_year.close()