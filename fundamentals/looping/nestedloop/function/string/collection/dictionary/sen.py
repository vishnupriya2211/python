sen = "hello vishnu priya , hello how are you"

words = sen.split()

word_count = {word: words.count(word) for word in words}

print(word_count)
