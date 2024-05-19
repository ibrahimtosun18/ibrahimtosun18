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

    # Ensure the column and row indices are within the board boundaries
    if col < 1 or col > 10 or row < 1 or row > 10:
        print("Move is out of board boundaries")
        sys.exit(1)

    # Debug: Print before updating the board
    print("Board before update:")
    for line in readme:
        print(line, end='')

    # Update the board
    updated = False
    for i, line in enumerate(readme):
        if i == row + 2:  # Adjust for the header lines
            parts = line.split('|')
            if col < len(parts):
                # Debug: Print the line before modification
                print(f"Line before modification: {line.strip()}")
                parts[col] = '🔥'
                readme[i] = '|'.join(parts) + '\n'
                updated = True
                # Debug: Print the line after modification
                print(f"Line after modification: {readme[i].strip()}")

    if not updated:
        print("No updates made to the board.")
        sys.exit(1)

    with open("README.md", "w") as file:
        file.writelines(readme)

    # Debug: Print updated README content
    print("Board after update:")
    with open("README.md", "r") as file:
        updated_content = file.read()
        print(updated_content)

if __name__ == "__main__":
    move = sys.argv[1]
    update_readme(move)
