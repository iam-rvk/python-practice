# Simple file operations example

# Write to a file
with open("demo.txt", "w") as f:
    f.write("Hello\n")
    f.write("This is a simple file example.\n")

# Read from the file
with open("demo.txt", "r") as f:
    data = f.read()

print("File content:")
print(data)
