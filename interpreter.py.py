import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python interpreter.py <filename>.emo")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            # Step 1: Bring in the program code and convert it to a string
            program_string = file.read()
            
        # For now, we will just print the string to confirm it was read correctly
        print("Program Loaded Successfully:")
        print(program_string)
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    main()