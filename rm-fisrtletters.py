text = input("Enter a sentence: ")

result = " ".join(word[1:] if len(word) > 0 else "" for word in text.split())

print("Output:", result)
