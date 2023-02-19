import io
import re
import string
import sys
import chardet
import concurrent.futures
from tqdm import tqdm

def detect_encoding(filepath):
    with open(filepath, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def process_file(filepath):
    # detect the encoding of the file
    encoding = detect_encoding(filepath)
    words = {}
    with open(filepath, "r", encoding=encoding, errors='ignore') as file:
        for line in tqdm(file, desc="Processing file"):
            # remove any punctuation from the file
            line = line.translate(str.maketrans("", "", string.punctuation))
            # split the contents into a list of words
            words_in_line = re.findall(r"[a-zA-Z0-9]+",line)
            for word in words_in_line:
                words[word] = None
    return words

def main():
    if len(sys.argv) < 4:
        print("Please specify the input and output file paths")
        return

    # read the input file paths
    filepath1 = sys.argv[1]
    filepath2 = sys.argv[2]

    # read the output file path
    outputfile = sys.argv[3]

    with tqdm(total=3, desc="Processing...") as pbar:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future1 = executor.submit(process_file, filepath1)
            future2 = executor.submit(process_file, filepath2)
        words = {**future1.result(), **future2.result()}
        pbar.update(1)
        # sort the words alphabetically
        words = sorted(words.keys())
        pbar.update(1)
    # write the processed words to a new file
    with open(outputfile, "w", encoding='utf-8') as file:
        for word in tqdm(words, desc="Writing to file"):
            file.write(word + " ")
            file.write('\n')
            pbar.update(1)
    with io.open(outputfile, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(outputfile, 'w') as f:
        for line in tqdm(lines, desc="Cleaning file", unit="line"):
            if line.strip() and re.search("^[a-zA-Z0-9_.,!?@#$%^&*()-=+ ]*$", line):
                f.write(line.rstrip()+'\n')
        pbar.update(1)
        
if __name__ == "__main__":
    main()
