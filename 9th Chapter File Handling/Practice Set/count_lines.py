import sys

def count_lines(filename):
    with open(filename, "r") as f:
        return len(f.readlines())
    
if __name__ == "__main__" :
    filename = sys.argv[1]
    line_count = count_lines(filename)
    print(f"The file {filename} has {line_count} lines.")