import os

def find_highest_gwa(filename):
    best_name = ""
    best_gwa = float('inf')

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            
            if len(parts) < 2:
                continue

            name = parts[0]
            gwa = float(parts[1])

            if gwa < best_gwa:
                best_gwa = gwa
                best_name = name

    return best_name, best_gwa


base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path, "students.txt")


name, gwa = find_highest_gwa(file_path)

print("Student with lowest GWA:")
print(name, "-", gwa)