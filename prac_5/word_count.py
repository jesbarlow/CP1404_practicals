sentence = input("Enter a sentence:")
words = sentence.split()
counting = {}

for word in words:
    if word in counting:
        counting[word] += 1
    else:
        counting[word] = 1

print("Text: {}".format(sentence))

for key, value in counting.items():
    print("{} : {}".format(key,value))