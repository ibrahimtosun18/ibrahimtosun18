import re
import sys

def update_readme(move):
    with open("README.md", "r") as file:
        readme_content = file.readlines()

    move_re = re.match(r"battleship\|attack\|([a-j])([0-9])", move, re.IGNORECASE)
    if move_re:
        col = ord(move_re.group(1).upper()) - ord('A') + 1
        row = int(move_re.group(2))

        # Find the board start and end positions
        try:
            board_start = readme_content.index("|   | A | B | C | D | E | F | G | H | I | J |\n") + 2
            board_end = board_start + 10
        except ValueError:
            print("Error: Could not find the board in README.md")
            return

        board_lines = readme_content[board_start:board_end]

        # Print board before modification
        print("Board before update:")
        for line in board_lines:
            print(line.strip())

        for i, line in enumerate(board_lines):
            if i + 1 == row:
                parts = line.strip().split(" | ")
                parts[col] = '🔥'
                board_lines[i] = " | ".join(parts) + "\n"
                print(f"Line before modification: {line.strip()}")
                print(f"Line after modification: {board_lines[i].strip()}")

        readme_content[board_start:board_end] = board_lines

        # Print board after modification
        print("Board after update:")
        for line in board_lines:
            print(line.strip())

    with open("README.md", "w") as file:
        file.writelines(readme_content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a move as an argument.")
        sys.exit(1)
    move = sys.argv[1]
    print(f"Received move: {move}")
    update_readme(move)
