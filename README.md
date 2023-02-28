<a id="top"></a>

#

<h1 align="center">
Combine Wordlist
</h1>

<p align="center"> 
  <kbd>
<img src="https://raw.githubusercontent.com/r0xd4n3t/combine-wordlist/main/img/combine-wordlist.png"></img>
  </kbd>
</p>

<p align="center">
<img src="https://img.shields.io/github/last-commit/r0xd4n3t/combine-wordlist?style=flat">
<img src="https://img.shields.io/github/stars/r0xd4n3t/combine-wordlist?color=brightgreen">
<img src="https://img.shields.io/github/forks/r0xd4n3t/combine-wordlist?color=brightgreen">
</p>

# Combine Wordlist

This Python code reads two input files, processes their contents to extract unique words, combines the unique words, and writes them to an output file. The code also cleans the output file by removing any lines that contain non-alphanumeric characters. 

**Free up some space by merging dictionaries!**

## Usage:

The code can be executed in the command line as follows:

```python combine.py <input-file-path-1> <input-file-path-2> <output-file-path>```

where `<input-file-path-1>` and `<input-file-path-2>` are the paths to the input files to be processed, and `<output-file-path>` is the path to the output file.

Example:
```python combine.py rockyou1.txt rockyou2.txt wer0xyou.txt```


## Prerequisites:

-   Python 3.x
-   tqdm (Python library for adding progress bars to loops) It can be installed via pip as follows:
```pip install tqdm```
-   chardet (Python library for detecting the encoding of a file) It can be installed via pip as follows:
```pip install chardet```
