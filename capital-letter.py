text = input("Enter a sentence: ")

result = " ".join(word.capitalize() for word in text.split())

print("Output:", result)