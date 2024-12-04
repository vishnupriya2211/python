f=open("C:\\Users\\micvi\\OneDrive\\Desktop\\pythonworks\\fundamentals\\looping\\nestedloop\\function\\string\\collection\\dictionary\\nested collection\\database\\student.txt","r")

s=open("C:\\Users\\micvi\\OneDrive\\Desktop\\pythonworks\\fundamentals\\looping\\nestedloop\\function\\string\\collection\\dictionary\\nested collection\\database\\fail.txt","r")

for_all_sut_set=set()

fail_stu_set=set()
for line in f:

    line=line.rstrip("\n")

    for_all_sut_set.add(line)
for line in s:

    line=line.rstrip("\n")

    fail_stu_set.add(line)

passed_student=for_all_sut_set.difference(fail_stu_set)


print(passed_student)