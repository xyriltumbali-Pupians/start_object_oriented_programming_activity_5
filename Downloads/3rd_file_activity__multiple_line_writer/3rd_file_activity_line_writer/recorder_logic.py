import os

class LifeRecorder:
    def __init__(self, filename="mylife.txt"):
        # Kunin kung saan naka-locate ang script file
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(base_path, filename)

    def write_multiple_lines(self):
        print("--- Writing Mode Active ---")
        print("Saving to:", self.filename)

        with open(self.filename, "a") as file:  # gamit 'a' para hindi mabura previous
            while True:
                line = input("Enter line: ")
                file.write(line + "\n")

                choice = input("Are there more lines y/n? ").lower()
                if choice != 'y':
                    break

        print(f"Successfully saved to {self.filename}")