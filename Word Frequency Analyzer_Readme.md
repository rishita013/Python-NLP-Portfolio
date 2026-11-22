# Word Frequency Analyzer

## Project Overview

The **Word Frequency Analyzer** is a Python-based Natural Language Processing (NLP) project that analyzes text and identifies the most frequently occurring words.

It uses the NLTK library for text tokenization and stopword removal, and Python's Counter class to calculate word frequencies.

This project is part of my journey learning Python and Natural Language Processing.

## Features

- Accepts text from the user.
- Converts text into lowercase.
- Tokenizes text into individual words using NLTK.
- Removes punctuation.
- Removes English stopwords.
- Counts word frequencies using `Counter`.
- Sorts words according to their frequency.
- Allows users to display their desired number of top words.
- Handles invalid numeric input using `try` and `except`.
- Validates that the requested number of words is greater than zero.

## Technologies Used

- Python
- NLTK (Natural Language Toolkit)
- Collections – Counter
- String – Punctuation

## Installation and Setup

### 1. Install Python

Download and install Python from [python.org](https://www.python.org/).

### 2. Install NLTK

Open your terminal and run:

```bash
pip install nltk
```

### 3. Download NLTK Resources

Run the following Python commands:

```python
import nltk

nltk.download('punkt_tab')
nltk.download('stopwords')
```

If your NLTK installation requires the older `punkt` resource, download that as well:

```python
nltk.download('punkt')
```

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python WFA.py
```

5. Enter your text when prompted.
6. Enter the number of top words you want to display.

## Example

**Input:**

```text
Python is a useful programming language.
Python is also interesting and easy to learn.
NLP is a branch of computer science.
```

**Number of top words:** `3`

**Output:**

```text
python : 2
useful : 1
programming : 1
```

## Python Concepts Learned

Through this project, I practised:

- Variables and data types
- String methods (`lower()`)
- Tokenization
- Lists and sets
- For loops and conditional statements
- List filtering
- Dictionaries and frequency counting
- `Counter` and `most_common()`
- Exception handling (`try` and `except`)
- Input validation

## Learning Outcome

This project helped me understand the basic steps involved in text preprocessing and word frequency analysis using Python and NLTK.

It is my second project in my 16-week Python for NLP learning journey.

## Future Improvements

- Save word frequency results to a text or CSV file.
- Display word frequencies using visual charts.
- Support multiple languages.
- Improve punctuation and text cleaning.

---

**Author:** Python for Linguistics Learning Journey  
**Project:** Week 2 – Word Frequency Analyzer
