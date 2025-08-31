import os
import sys

def get_root_directory() -> str:
    return input("Enter the full path to the root folder: ")


def check_file_handle_exceptions(file_full_path: str) -> None:
    if os.path.exists(file_full_path):
        print(f"File '{file_full_path}' already exists, do you want to replace it? (y/n)")
        choice = input().lower()

        if choice == "y":
            try:
                os.remove(file_full_path)
                print(f"Old file '{file_full_path}' removed.")
            except OSError as e:
                print(f"Error removing file: {e}")
                sys.exit(1)

        elif choice == "n":
            print("Operation cancelled. Program terminated.")
            sys.exit(0)

        else:
            print("Unknown option. Program terminated.")
            sys.exit(1)


def write_file(directory: str, file_full_path: str) -> None:
    folders_to_ignore = {'venv', '.venv', '__pycache__'}

    try:
        with open(file_full_path, "w") as f:
            f.write(f"Python files found in: {directory}\n\n")

            for dirpath_to_current_folder, dir_names_in_current_folder, filenames in os.walk(directory):
                # This line modifies dirnames_in_current_folder in place, preventing os.walk to enter unwanted directories.
                dir_names_in_current_folder[:] = [name for name in dir_names_in_current_folder if name not in folders_to_ignore and not name.startswith('.')]
                for filename in filenames:
                    if filename.endswith(".py"):
                        f.write(f'{filename}\n')

        print("Finished.")

    except IOError as e:
        print(f"Error: Could not write to file. {e}")
        sys.exit(1)


def main():
    directory = get_root_directory()

    filename = "python_files_list.txt"
    file_full_path = os.path.join(directory, filename)

    check_file_handle_exceptions(file_full_path)
    write_file(directory, file_full_path)


if __name__ == "__main__":
    main()