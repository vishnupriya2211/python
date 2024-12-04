order=["tea","coffees","tea","coffees","gheeroast","plainroast","porotta","tea"]

oder_summary={}

for s in order:

    if s in oder_summary:

     oder_summary[s]+=1

    else:
         oder_summary[s]=1
print(oder_summary)

