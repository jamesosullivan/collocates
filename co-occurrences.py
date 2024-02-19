import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Ensure necessary resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

def co_occurrence(text, window_size=2):
    # Load stopwords
    stop_words = set(stopwords.words('english'))
    
    # Tokenize the text and filter out stopwords
    tokens = [token.lower() for token in word_tokenize(text) if token.isalpha() and token.lower() not in stop_words]
    
    # Initialize co-occurrence count
    co_occurrence_counts = Counter()
    
    # Calculate co-occurrences within the specified window size
    for i in range(len(tokens)):
        token = tokens[i]
        start = max(0, i - window_size)
        end = min(len(tokens), i + window_size + 1)
        for j in range(start, end):
            if i != j:
                co_occurred_token = tokens[j]
                co_occurrence_counts[(token, co_occurred_token)] += 1
    
    # Return the top 10 most common co-occurrences
    return co_occurrence_counts.most_common(10)

# Read the text file
with open("text-file-here.txt", "r", encoding='utf-8') as file:
    text = file.read()

# Calculate the top 10 co-occurrences
top_co_occurrences = co_occurrence(text, window_size=2)

# Output the results
with open("top-co-occurrence-results.txt", "w", encoding='utf-8') as output_file:
    for pair, freq in top_co_occurrences:
        output_file.write(f"{pair[0]}, {pair[1]}: {freq}\n")

print("Top 10 co-occurrence analysis is complete. Results are saved in 'top-co-occurrence-results.txt'.")
