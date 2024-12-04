def review (rating):
    if rating <0:
        raise Exception ("too low")
    
    else:

        print("done!")

try:

    review(-1)

except Exception as e:

    print(e)

print("file operation")

print("database commit")
