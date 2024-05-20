import sys

def update_readme(move):
    move = move.strip().lower()
    parts = move.split("|")
    action = parts[1]
    position = parts[2]

    column = position[0]
    row = position[1]

    columns = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    col = columns.index(column)
    row = int(row)

    with open("README.md", "r") as file:
        lines = file.readlines()

    print(f"Received move: {move}")
    print(f"Parsed move: column {col + 1}, row {row}")

    found = False
    for i in range(len(lines)):
        if lines[i].startswith(f"| {row} |"):
            print(f"Line before modification: {lines[i].strip()}")
            parts = lines[i].split(" | ")
            parts[col + 1] = "🔥" if parts[col + 1] == "🚢" else "❌"
            lines[i] = " | ".join(parts) + "\n"
            print(f"Line after modification: {lines[i].strip()}")
            found = True
            break

    if not found:
        print("No updates made to the board.")
        sys.exit(1)

    with open("README.md", "w") as file:
        file.writelines(lines)

if __name__ == "__main__":
    move = sys.argv[1]
    update_readme(move)
