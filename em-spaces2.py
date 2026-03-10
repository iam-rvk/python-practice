# Remove all spaces from a paragraph

text = input("Enter paragraph: ")
#result = text.replace(" ", "")
result = "".join(text.split())


print("Output:")
print(result)