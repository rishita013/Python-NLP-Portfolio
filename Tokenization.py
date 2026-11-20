import nltk
from nltk import sent_tokenize, word_tokenize
text = input("Enter your text here: ")

#Sentence Split
sentences = sent_tokenize(text)
print(len(sentences))
print("sentences: ", sentences)
for index,sentences in enumerate (sentences, start=1):
    print (f"sentences: {index}: ", sentences)

#Word Spliting
words= word_tokenize(text)
print(len(words))
print("words: ", words)
for index,words in enumerate (words, start=1):
    print (f"words: {index}: ", words)