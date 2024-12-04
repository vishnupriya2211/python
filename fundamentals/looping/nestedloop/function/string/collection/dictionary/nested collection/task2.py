student_data= {
    "vishnu":[45,35,55],
    "priya":[45,25,65],
    "anupama":[25,55,15],
    "sonu":[75,85,95],
    "prakrithi":[55,45,25],

}

#index=4
#for i,element in enumerate(student_data):
 #   if i+1 ==index:
  #      print(element)
   #     marks=student_data.get(element)
    #    avg=sum(marks)/len(marks)
     #   print(avg)

student_avg_mark={k:sum(v)/len(v) for k,v in student_data.items()}

print(student_avg_mark)         