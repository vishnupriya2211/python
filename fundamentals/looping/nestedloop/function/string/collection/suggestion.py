users=["priya","anupama","prakrithi","nandhu","revathy","nandhana"]

priya_followers=["nandhu","anupama","prakrithi","priya"]

anupama_followers=["revathy","anupama","prakrithi","nandhu"]


mutual_followers=set(priya_followers).intersection(set(anupama_followers))

print(mutual_followers)