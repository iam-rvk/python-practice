text = input("Enter text: ")

words = text.split()
unique_words = list(dict.fromkeys(words))  # keeps original order

result = " ".join(unique_words)
print("Output:", result)
