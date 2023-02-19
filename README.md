# combine-word

This Python code reads two input files, processes their contents to extract unique words, combines the unique words, and writes them to an output file. The code also cleans the output file by removing any lines that contain non-alphanumeric characters. 

**Free up some space by merging dictionaries!**

## Usage:

The code can be executed in the command line as follows:

```python <path-to-python-file> <input-file-path-1> <input-file-path-2> <output-file-path>```

where `<path-to-python-file>` is the path to the Python file containing the code, `<input-file-path-1>` and `<input-file-path-2>` are the paths to the input files to be processed, and `<output-file-path>` is the path to the output file.

Example:
```python combine.py rockyou1.txt rockyou2.txt wer0xyou.txt```


## Prerequisites:

-   Python 3.x
-   tqdm (Python library for adding progress bars to loops) It can be installed via pip as follows:
```pip install tqdm```
-   chardet (Python library for detecting the encoding of a file) It can be installed via pip as follows:
```pip install chardet```
