import os

class MyLifeWriter:
    def __init__(self, filename="mylife.txt"):
        # Save file in the SAME folder as this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(script_dir, filename)

    def get_lines(self):
        lines = []

        while True:
            line = input("Enter line: ")
            lines.append(line)

            more = input("Are there more lines y/n? ").lower()
            if more != 'y':
                break

        return lines

    def write_to_file(self, lines):
        with open(self.filename, "w", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")

    def run(self):
        print("Current working directory:", os.getcwd())

        lines = self.get_lines()
        self.write_to_file(lines)

        print("Saved successfully!")
        print("File location:", self.filename)

if __name__ == "__main__":
    writer = MyLifeWriter()
    writer.run()