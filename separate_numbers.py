import os

base_path = os.path.dirname(__file__)

input_file = os.path.join(base_path, "numbers.txt")

even_numbers = []
odd_numbers = []

with open(input_file, "r") as infile:
    numbers = infile.readlines()

for num in numbers:
    num = int(num.strip())

    if num % 2 == 0:
        even_numbers.append(str(num))
    else:
        odd_numbers.append(str(num))

even_file_path = os.path.join(base_path, "even.txt")
odd_file_path = os.path.join(base_path, "odd.txt")

with open(even_file_path, "w") as even_file:
    even_file.write("\n".join(even_numbers))

with open(odd_file_path, "w") as odd_file:
    odd_file.write("\n".join(odd_numbers))

print("Done! Check even.txt and odd.txt.")