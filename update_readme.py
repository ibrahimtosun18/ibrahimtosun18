import sys
import re

def update_readme(move):
    with open("README.md", "r") as file:
        readme = file.readlines()

    # Debug: Print the move received
    print(f"Received move: {move}")

    # Parse the move
    match = re.match(r'battleship\|attack\|([a-j])([1-9]|10)', move)
    if not match:
        print("Invalid move format")
        sys.exit(1)
    
    col, row = match.groups()
    col = ord(col.upper()) - ord('A') + 1
    row = int(row)

    # Debug: Print parsed column and row
    print(f"Parsed move: column {col}, row {row}")

    # Update the board
    for i, line in enumerate(readme):
        if i == row + 2:
            parts = line.split('|')
            parts[col] = '🔥'
            readme[i] = '|'.join(parts)

    with open("README.md", "w") as file:
        file.writelines(readme)

    # Debug: Print updated README content
    with open("README.md", "r") as file:
        print(file.read())

if __name__ == "__main__":
    move = sys.argv[1]
    update_readme(move)
