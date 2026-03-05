numbers = []
i = 1

# Create list from 1 to 55
while i <= 55:
    numbers.append(i)
    i += 1

# Eliminate odd numbers
even_numbers = []
j = 0
while j < len(numbers):
    if numbers[j] % 2 == 0:
        even_numbers.append(numbers[j])
    j += 1

print(even_numbers)
