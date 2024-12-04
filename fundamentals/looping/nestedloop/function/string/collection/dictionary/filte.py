scores = { "anupama": 45,"prakrithi": 67,"nandhu": 85,"ks": 30,"ambady": 92 }

filtered_scores = {key: value for key, value in scores.items() if value > 50}

print(filtered_scores)
