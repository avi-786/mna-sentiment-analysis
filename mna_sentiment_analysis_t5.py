#   Data Analysis, Transformation & Visualisation Libraries
import pandas as pd
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import re
from collections import Counter

#   Model training and Dataloader libraries
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments, TrainerCallback
from datasets import Dataset, DatasetDict
evaluation_data = pd.read_csv('train.csv')
#evaluation_data = evaluation_data.iloc[]
evaluation_data

from collections import Counter

# Optional: set pandas to show all rows (though here we'll only print top 50)
pd.set_option('display.max_rows', None)

# Common stop words to remove
stop_words = {"the", "in", "to", "or", "of", "and", "a", "for", "on", "with", "at", "by", "from", "as", "an", "is", "it", "this", "that", "be", "which"}

# Load dataset from Google Drive (adjust the file path as needed)
file_path = '/content/drive/MyDrive/Colab Notebooks/train.csv'  # update this path to match where your file is stored
df = pd.read_csv(file_path)

# Check if the "Deal Synopsis" column exists
if "Deal Synopsis" in df.columns:
    # 1) Combine all non-null entries in the "Deal Synopsis" column into a single string
    all_text = ' '.join(df['Deal Synopsis'].dropna().tolist())
else:
    raise ValueError(f"'Deal Synopsis' column not found in the dataset. Available columns: {df.columns.tolist()}")

# 2) Clean the text: convert to lower case and remove punctuation
all_text_clean = re.sub(r'[^\w\s]', '', all_text.lower())

# 3) Split the cleaned text into individual words
words = all_text_clean.split()

# 4) Filter out the unwanted stop words
words = [w for w in words if w not in stop_words]

# 5) Count the frequency of each remaining word
unique_values = pd.Series(words).value_counts()

# Print only the top 50 words
print("Top 50 words:\n", unique_values.head(50))

# Print how many times 'merger' appears
merger_count = unique_values.get('synergy', 0)
print(f"\nNumber of times 'merger' appears: {merger_count}")
# Assuming evaluation_data is already loaded from '/content/drive/MyDrive/Colab Notebooks/train.csv'

# Prompt the user for the word to search (case-insensitive)
word = input("Enter the word for frequency analysis: ").strip().lower()

# Dictionary to store frequency count for each column that holds text data
freq_counts = {}

# Iterate over all columns in the DataFrame
for col in evaluation_data.columns:
    # Process only object-type columns (usually text)
    if evaluation_data[col].dtype == 'object':
        # Convert column values to string, lower-case them, and count occurrences of the word
        count = evaluation_data[col].astype(str).str.lower().str.count(word).sum()
        freq_counts[col] = count

# Sort the results by frequency (descending order)
sorted_freq = sorted(freq_counts.items(), key=lambda x: x[1], reverse=True)

# Convert sorted result into a DataFrame for a neat row-wise display
result_df = pd.DataFrame(sorted_freq, columns=['Column', 'Frequency'])

print("\nFrequency of the word '{}' in each text column (sorted descending):".format(word))
print(result_df)

