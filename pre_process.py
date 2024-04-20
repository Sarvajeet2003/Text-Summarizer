import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load the dataset
df = pd.read_csv('/Users/sarvajeethuk/Downloads/IR/Assignment_4/archive-2/Reviews.csv')

# Define function for text cleaning and preprocessing
def clean_text(text):
    # Check if text is NaN
    if pd.isnull(text):
        return ''
    # Convert text to lowercase
    text = text.lower()
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokenize text
    tokens = word_tokenize(text)
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    # Join tokens back into text
    cleaned_text = ' '.join(tokens)
    return cleaned_text

# Apply cleaning function to 'Text' and 'Summary' columns
df['Cleaned_Text'] = df['Text'].apply(clean_text)
df['Cleaned_Summary'] = df['Summary'].apply(clean_text)

# Save cleaned dataset to a new CSV file
df.to_csv('cleaned_dataset.csv', index=False)
