import os
import sys

def main():
    directory = input("Enter the full path to root folder: ")

    filename = "python_files_list.txt"
    folders_to_ignore = {'venv', '.venv', '__pycache__'}
    output_path = os.path.join(directory, filename)

    if os.path.exists(output_path):
        print(f"File '{output_path}' already exists, do you want to replace it? (y/n)")
        choice = input().lower()
        if choice == "y":
            try:
                os.remove(output_path)
                print(f"Old file '{output_path}' removed.")
            except OSError as e:
                print(f"Error removing file: {e}")
                sys.exit(1)
        elif choice == "n":
            print("Operation cancelled. Program terminated.")
            sys.exit(0)
        else:
            print("Unknown option. Program terminated.")
            sys.exit(1)

    try:
        with open(output_path, "w") as f:
            f.write(f"Python files found in: {directory}\n\n")
            for dirpath, dirnames, filenames in os.walk(directory):
                #Ignore the unwanted folders.
                dirnames[:] = [name for name in dirnames if name not in folders_to_ignore]
                for filename in filenames:
                    if filename.endswith(".py"):
                        f.write(f'{filename}\n')

        print("Finished.")

    except IOError as e:
        print(f"Error: Could not write to file. {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()