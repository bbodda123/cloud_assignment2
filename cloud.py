import nltk
from nltk.corpus import webtext
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('webtext')
nltk.download('punkt')
english_stops = set(stopwords.words('english'))
print(english_stops)
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
file_path = "random_paragraphs.txt"
    # Read the contents of the file
text = read_file(file_path)
print(text)

from nltk.tokenize import word_tokenize,sent_tokenize
words= word_tokenize(text)
tokenize_words_without_stop_words = []
for word in words:
    if word not in english_stops:
        tokenize_words_without_stop_words.append(word)
        
print(tokenize_words_without_stop_words[0:50])
l=tokenize_words_without_stop_words
d={}
for i in l :
    if i not in d.keys():
        d[i] =0
    d[i] = d[i]+1
print(d)
        