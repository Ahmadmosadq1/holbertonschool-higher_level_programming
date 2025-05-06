# Python - Hello, World

This is the first Python project in the Holberton School curriculum.  
It introduces basic Python syntax, string manipulation, formatting, and style standards using `pycodestyle`.

---

## 📚 Learning Objectives

By completing this project, you will be able to:

- Run and write Python scripts using the command line
- Use the `print()` function with both static strings and variables
- Manipulate strings using indexing and slicing
- Apply proper Python coding style using `pycodestyle`
- Understand the concept of script execution and file permissions in Linux

---

## 🧰 Requirements

- Python 3.8.x
- All scripts must start with `#!/usr/bin/python3`
- Files must be executable: use `chmod +x filename.py`
- Follow `pycodestyle` version 2.7.*
- No unnecessary semicolons, loops, or conditionals (unless stated)
- Files checked with `wc` for line/character limits

---

## 📁 Files and Descriptions

| File Name           | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `2-print.py`        | Prints a static string using `print()`:  
`"Programming is like building a multilingual puzzle"` |
| `3-print_number.py` | Prints an integer using **f-string** without casting:  
`98 Battery street` |
| `4-print_float.py`  | Prints a float with 2 decimal places using f-strings:  
`Float: 3.14` |
| `5-print_string.py` | Prints a string three times, followed by its first 9 characters |
| `6-concat.py`       | Concatenates two strings (`str1` + `str2`) to print:  
`Welcome to Holberton School!` |
| `7-edges.py`        | Demonstrates slicing:  
prints first 3, last 2, and middle of a string |
| `8-concat_edges.py` | Extracts and concatenates parts of a string to form:  
`object-oriented programming with Python` |
| `9-easter_egg.py`   | Uses a Python **Easter Egg** to print “The Zen of Python” by importing `this` |

---

## 🔍 Style Guide

All code has been formatted using **PEP8** standards and verified with:

```bash
pycodestyle <filename.py>

