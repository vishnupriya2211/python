from json import load

f=open("C:\\Users\\micvi\\OneDrive\\Desktop\\pythonworks\\fundamentals\\looping\\nestedloop\\function\\string\\collection\\dictionary\\nested collection\\dataset\\country.json",encoding="utf-8")

data=load(f)

print(len(data))

#all_country_name=[country.get("name") for country in data]

#print(all_country_name)

all_regions=[regions.get("region") for regions in data]

#print(set(all_regions))

region_count={region:all_regions.count(region) for region in all_regions}

#print(region_count)

max_region_count=max(region_count,key=lambda k:region_count.get(k))

#print(max_region_count,region_count.get(max_region_count))

capital=[country.get("capital")for country in data if country.get("name")=="India"]

#print(capital)

country_border={country.get("name"):len(country.get("borders",[]))for country in data}

#print(country_border)

max_boredr_country=max(data,key=lambda country :len(country.get("borders",[]))).get("name")

#print(max_boredr_country)

most_populated=max(data,key=lambda country:country.get("population",0)).get("name")

#print(most_populated)

alpha_three=[country.get("borders")for country in data if country.get("name")=="India"][0]

for code in alpha_three:
    if country_border.get("alpha3code")==
   

print(country_border)
