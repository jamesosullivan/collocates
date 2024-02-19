import nltk
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure necessary resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

def perform_collocation_analysis(file_path):
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Convert to lower case and filter out non-alphabetic tokens
    words = [word.lower() for word in tokens if word.isalpha()]
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    
    # Setup Bigram Finder
    bigram_measures = BigramAssocMeasures()
    bigram_finder = BigramCollocationFinder.from_words(words)
    
    # Setup Trigram Finder
    trigram_measures = TrigramAssocMeasures()
    trigram_finder = TrigramCollocationFinder.from_words(words)
    
    # Find the top 10 bigrams and trigrams using the PMI measure
    top_bigrams = bigram_finder.nbest(bigram_measures.pmi, 10)
    top_trigrams = trigram_finder.nbest(trigram_measures.pmi, 10)
    
    return top_bigrams, top_trigrams

# Path to your input file
file_path = "text-file-here.txt"

# Perform the analysis
top_bigrams, top_trigrams = perform_collocation_analysis(file_path)

# Output the results to a text file, clearly separating bigrams and trigrams
with open("collocation-results.txt", "w", encoding='utf-8') as output_file:
    output_file.write("Top 10 Bigram Collocations:\n")
    for bigram in top_bigrams:
        output_file.write(f"{bigram[0]} {bigram[1]}\n")
    output_file.write("\nTop 10 Trigram Collocations:\n")
    for trigram in top_trigrams:
        output_file.write(f"{trigram[0]} {trigram[1]} {trigram[2]}\n")

print("Collocation analysis is complete. Results are clearly separated in 'collocation-results.txt'.")
