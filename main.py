# This is a Python script to compare two text files and show their diff
#

import argparse

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # Compare the lines
    num_lines = max(len(lines1), len(lines2))
    for i in range(num_lines):
        line1 = lines1[i].strip() if i < len(lines1) else ''
        line2 = lines2[i].strip() if i < len(lines2) else ''

        if line1 != line2:
            print(f"Line {i+1}:")
            print(f"   {file1}: {line1}")
            print(f"   {file2}: {line2}")
            print("")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Compare two text files line by line.")
    parser.add_argument('file1', type=str, help='First input file name')
    parser.add_argument('file2', type=str, help='Second input file name')
    args = parser.parse_args()

    # Call compare_files with the provided file names
    compare_files(args.file1, args.file2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
