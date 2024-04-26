import nltk
from nltk.corpus import webtext
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('webtext')
nltk.download('punkt')
english_stops = set(stopwords.words('english'))
print(english_stops)
def read_file_path(file_path):
    with open(file_path, 'r') as file:
        return file.read()
file = "random_paragraphs.txt"
    # Read the contents of the file
text = read_file_path(file)
print(text)

from nltk.tokenize import word_tokenize,sent_tokenize
words= word_tokenize(text)
tokenize_words_without_stop_words = []
for word in words:
    if word not in english_stops:
        tokenize_words_without_stop_words.append(word)
        
print(tokenize_words_without_stop_words[0:50])
tokenize_words_without_stop_words
dictionary={}
for i in tokenize_words_without_stop_words :
    if i not in dictionary.keys():
        dictionary[i] =0
    dictionary[i] = dictionary[i]+1
print(dictionary)
        
