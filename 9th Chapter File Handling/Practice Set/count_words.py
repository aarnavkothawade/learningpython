import sys 

def count_words(filename, word):
    with open(filename, "r") as f:
        counter = 0
        for line in f:
            words = line.split()
            for w in words:
                if w == word:
                    counter += 1
        return counter


if __name__ == "__main__":
    filename = sys.argv[1]
    word = sys.argv[2]
    word_count = count_words(filename, word)
    print(f"The file {filename} has {word_count} {word}.")
