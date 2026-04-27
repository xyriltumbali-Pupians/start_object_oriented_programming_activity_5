import os

def process_integers():
    try:
        base_path = os.path.dirname(__file__)

        input_file = os.path.join(base_path, "integers.txt")
        output_even = os.path.join(base_path, "double.txt")
        output_odd = os.path.join(base_path, "triple.txt")

        with open(input_file, "r") as infile, \
             open(output_even, "w") as even_file, \
             open(output_odd, "w") as odd_file:

            for line in infile:
                num = int(line.strip())

                if num % 2 == 0:
                    even_file.write(f"{num**2}\n")
                else:
                    odd_file.write(f"{num**3}\n")

        print("Files created successfully.")

    except FileNotFoundError:
        print("Error: integers.txt not found.")
    except ValueError:
        print("Error: File contains non-integer values.")

process_integers()