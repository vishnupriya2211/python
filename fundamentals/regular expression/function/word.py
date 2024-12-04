
text = "this is a simple python program that print most recursive word . this program is simple"
words = text.lower().split()
word_count = {}

for word in words:
   
    if word in word_count:
        word_count[word] += 1
    else:
       
        word_count[word] = 1
frequent_word = max(word_count, key=word_count.get)
frequency = word_count[frequent_word]
print(f"The most frequent word is: '{frequent_word}' count {frequency}")
