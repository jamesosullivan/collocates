import nltk
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure necessary resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

def perform_collocation_analysis(file_path):
    """Perform collocation analysis on a given text file to find top bigrams and trigrams, excluding those that occur only once."""
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text, remove non-alphabetic tokens, and convert to lowercase
    tokens = word_tokenize(text)
    words = [word.lower() for word in tokens if word.isalpha()]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]

    # Initialize Bigram and Trigram Finders
    bigram_measures = BigramAssocMeasures()
    trigram_measures = TrigramAssocMeasures()
    bigram_finder = BigramCollocationFinder.from_words(filtered_words)
    trigram_finder = TrigramCollocationFinder.from_words(filtered_words)

    # Apply frequency filter to exclude n-grams that occur only once
    bigram_finder.apply_freq_filter(2)
    trigram_finder.apply_freq_filter(2)

    # Find the top 10 bigrams and trigrams using PMI
    top_bigrams = bigram_finder.nbest(bigram_measures.pmi, 10)
    top_trigrams = trigram_finder.nbest(trigram_measures.pmi, 10)

    return top_bigrams, top_trigrams

file_path = "filename.txt"
top_bigrams, top_trigrams = perform_collocation_analysis(file_path)

# Writing results to file, separating bigrams and trigrams
with open("collocation-results.txt", "w", encoding='utf-8') as output_file:
    output_file.write("Top Bigram Collocations (excluding those occurring only once):\n")
    for bigram in top_bigrams:
        output_file.write(f"{bigram[0]} {bigram[1]}\n")
    output_file.write("\nTop Trigram Collocations (excluding those occurring only once):\n")
    for trigram in top_trigrams:
        output_file.write(f"{trigram[0]} {trigram[1]} {trigram[2]}\n")

print("Collocation analysis is complete. Results are saved in 'collocation-results.txt'.")
