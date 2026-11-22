
from nltk import word_tokenize
from string import punctuation
from collections import Counter
from nltk.corpus import stopwords

text = input("Please enter your text here: ")

try:
    top_n = int(input("How many top words do you want to display? "))

except ValueError:
    print("Please enter a valid number.")

else:
    if top_n <= 0:
        print("Please enter a value greater than 0.")

    else:
        # Convert text to lowercase
        text = text.lower()

        # Tokenization
        words = word_tokenize(text)

        # Get English stopwords
        stop_words = set(stopwords.words('english'))

        # Remove punctuation and stopwords
        filtered_words = []
        for word in words:
            if word not in punctuation and word not in stop_words:
                filtered_words.append(word)

        # Count word frequencies
        frequency = Counter(filtered_words)

        # Display top N words
        top_words = frequency.most_common(top_n)

        for word, count in top_words:
            print(word, ":", count)
