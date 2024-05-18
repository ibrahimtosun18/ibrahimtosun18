import sys
import re

def update_readme(move):
    with open("README.md", "r") as file:
        readme = file.readlines()

    # Parse the move
    match = re.match(r'battleship\|attack\|([a-j])([1-9]|10)', move)
    if not match:
        print("Invalid move format")
        sys.exit(1)
    
    col, row = match.groups()
    col = ord(col.upper()) - ord('A') + 1
    row = int(row)

    # Update the board
    for i, line in enumerate(readme):
        if i == row + 2:
            parts = line.split('|')
            parts[col] = '🔥'
            readme[i] = '|'.join(parts)

    with open("README.md", "w") as file:
        file.writelines(readme)

if __name__ == "__main__":
    move = sys.argv[1]
    update_readme(move)
