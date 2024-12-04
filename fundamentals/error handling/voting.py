def vote (age):
    if age <18:
        raise Exception ("invalid for voting")
    
    else:

        print("valid for voting")

try:
    vote(19)

except Exception as e:
    print(e)