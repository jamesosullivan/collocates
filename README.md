# Collocations & Co-occurrences

This repository contains two Python scripts designed for natural language processing (NLP) tasks, specifically focusing on collocation analysis and co-occurrence analysis of textual data. Both scripts are tailored to uncover linguistic patterns and relationships between words within a given text.

## 1. Collocation Analysis Script

### Purpose

The collocation analysis script identifies pairs (bigrams) and triplets (trigrams) of words that frequently occur together in the input text more often than would be expected by chance. Collocations are significant for understanding common word combinations that carry specific meanings or connotations.

### Requirements

- Python 3.x
- NLTK library (Natural Language Toolkit)

To install NLTK: Run `pip install nltk` in your terminal, and ensure you have downloaded the necessary NLTK data (`punkt` and `stopwords`) by executing the following Python commands:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### Usage

1. Save your input text in a file named `BarackObama1.txt`.
2. Run the script. It reads the input file, performs collocation analysis, and outputs the top 10 bigrams and trigrams.
3. Results are saved in `collocation-results.txt`, with bigrams and trigrams listed separately.

## 2. Co-occurrence Analysis Script

### Purpose

The co-occurrence analysis script examines the frequency of pairs of words appearing within a specified window size of each other in the text. This analysis helps identify words that are contextually related, providing insights into the thematic and semantic relationships within the text.

### Requirements

- Python 3.x
- NLTK library

Ensure the NLTK library is installed and the necessary data has been downloaded (as mentioned above).

### Usage

1. The script expects the text to be analysed in a file named `BarackObama1.txt`.
2. It calculates the co-occurrence of all word pairs, excluding stopwords, within a window size of 2 (this can be adjusted in the script).
3. The top 10 most common co-occurrences are output to `top-co-occurrence-results.txt`.

### How to Run the Scripts

- Ensure Python 3.x is installed on your machine.
- Place your input text file in the same directory as the scripts.
- Execute the scripts via the terminal or command prompt:
  
  For collocation analysis: `python collocation_analysis_script.py`
  
  For co-occurrence analysis: `python co_occurrence_analysis_script.py`

### Output

- **Collocation Analysis**: The output file `collocation-results.txt` will contain the top 10 bigrams and trigrams, each set separated by a blank line.
- **Co-occurrence Analysis**: The output file `top-co-occurrence-results.txt` will list the top 10 co-occurring word pairs with their frequency counts.

---

This README provides a concise overview of the scripts' functionalities and how to utilize them for analyzing textual data. For any additional details or troubleshooting, refer to the official [NLTK documentation](http://www.nltk.org/).