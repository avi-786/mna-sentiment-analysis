
# Prompt the user for the word to search (case-insensitive)
word = input("Enter the word for frequency analysis: ").strip().lower()

# Ensure required columns exist in the DataFrame
if "Deal Synopsis" not in evaluation_data.columns:
    raise ValueError("'Deal Synopsis' column not found in the dataset.")
if "Acquiror Macro Industry" not in evaluation_data.columns:
    raise ValueError("'Acquiror Macro Industry' column not found in the dataset.")

# List to hold results
results = []

# Iterate over each row in the DataFrame
for idx, row in evaluation_data.iterrows():
    # Get the deal synopsis text and ensure it's a string in lower case
    deal_synopsis = str(row["Deal Synopsis"]).lower()
    # Count the occurrences of the word in this row
    count = deal_synopsis.count(word)
    # If the word is found at least once, record the details
    if count > 0:
        results.append({
            "Row Number": idx,  # use idx (or idx+1 if you prefer row numbers starting at 1)
            "Frequency": count,
            "Acquirer Macro Industry": row["Acquiror Macro Industry"]
        })

# Convert the results into a DataFrame for neat display
result_df = pd.DataFrame(results)

# Print the results
if result_df.empty:
    print(f"No rows found with the word '{word}' in the 'Deal Synopsis' column.")
else:
    print(f"Rows where the word '{word}' appears in the 'Deal Synopsis' column:")
    print(result_df)
import re
from collections import Counter

# Ensure required columns exist in the DataFrame
required_columns = ["Deal Synopsis", "Target Macro Industry", "Acquiror Macro Industry"]
for col in required_columns:
    if col not in evaluation_data.columns:
        raise ValueError(f"'{col}' column not found in the dataset.")

# Prompt the user for Target Macro Industry and Acquiror Macro Industry (case-insensitive)
target_industry = input("Enter the Target Macro Industry: ").strip().lower()
acquiror_industry = input("Enter the Acquiror Macro Industry: ").strip().lower()

# Filter rows that match the provided industry inputs
filtered_data = evaluation_data[
    (evaluation_data["Target Macro Industry"].str.lower() == target_industry) &
    (evaluation_data["Acquiror Macro Industry"].str.lower() == acquiror_industry)
]

if filtered_data.empty:
    print("No rows found matching the provided industries.")
else:
    # Define common stop words to remove (you can extend this list as needed)
    stop_words = {"the", "in", "to", "or", "of", "and", "a", "for",
                  "on", "with", "at", "by", "from", "as", "an", "is",
                  "it", "this", "that", "be", "which"}

    results = []

    # Iterate over each relevant row
    for idx, row in filtered_data.iterrows():
        # Process the Deal Synopsis text: convert to lowercase and remove punctuation
        deal_text = str(row["Deal Synopsis"]).lower()
        deal_text_clean = re.sub(r'[^\w\s]', '', deal_text)

        # Split the text into individual words and remove stop words
        words = [word for word in deal_text_clean.split() if word not in stop_words]

        # Count the frequency of each word
        word_counts = Counter(words)

        # Extract the top 5 most common words
        top5 = word_counts.most_common(5)

        # Format the top 5 words as a string (word (count), ...)
        top5_str = ", ".join([f"{word} ({count})" for word, count in top5])

        results.append({
            "Row Number": idx,  # using the index; add +1 if you want row numbers starting at 1
            "Top 5 Words": top5_str
        })

    # Convert results to a DataFrame for neat display
    result_df = pd.DataFrame(results)
    print("Top 5 most used words in 'Deal Synopsis' for each relevant row:")
    print(result_df)
import re
import pandas as pd

# Define default stop words
stop_words = {"the", "in", "to", "or", "of", "and", "a", "for",
              "on", "with", "at", "by", "from", "as", "an", "is",
              "it", "this", "that", "be", "which"}

# Prompt the user to optionally add more stop words
user_stop_input = input("Enter additional stop words separated by commas (or press Enter to skip): ")
if user_stop_input.strip():
    new_stops = {w.strip().lower() for w in user_stop_input.split(',') if w.strip()}
    stop_words = stop_words.union(new_stops)  # Merge with existing set

# ------------------------------
# Subset Analysis (optional part)
# ------------------------------

# Prompt user for row range (0-indexed)
start_row = int(input("Enter the start row index: "))
end_row   = int(input("Enter the end row index: "))

# Prompt user for a word to see how often it appears in that subset
subset_word = input("Enter the word for which you want the frequency in the selected rows: ").strip().lower()

# Combine text from the specified rows in the "Deal Synopsis" column
subset_text = ' '.join(evaluation_data['Deal Synopsis'].iloc[start_row:end_row+1].dropna().tolist())
subset_text_clean = re.sub(r'[^\w\s]', '', subset_text.lower())
subset_words = [w for w in subset_text_clean.split() if w not in stop_words]

# Build a frequency table for the selected subset
subset_freq_table = pd.Series(subset_words).value_counts()

# Print the frequency of 'subset_word' in that partial subset
print(f"\n'{subset_word}' appears {subset_freq_table.get(subset_word, 0)} times in rows {start_row} to {end_row}.")

# Optionally, display the top 10 words in the selected subset
print("\nTop 10 words in the selected subset:")
print(subset_freq_table.head(10))

# ------------------------------
# Global Analysis: Row-by-Row Details
# ------------------------------

# Prompt user for a word to check its frequency across the entire dataset
global_word = input("\nEnter a word to check its frequency across the entire dataset: ").strip().lower()

# List to hold results for each row where the word is found
global_results = []

# Iterate over each row in the dataset to search for the word in "Deal Synopsis"
for idx, row in evaluation_data.iterrows():
    # Clean and process the deal synopsis text
    deal_text = str(row["Deal Synopsis"]).lower()
    deal_text_clean = re.sub(r'[^\w\s]', '', deal_text)
    words = [w for w in deal_text_clean.split() if w not in stop_words]

    # Count the occurrences of the global word in this row
    count = words.count(global_word)

    # If the word is found, record the row number, frequency, and Acquiror Macro Industry
    if count > 0:
        global_results.append({
            "Row Number": idx,  # Use idx (or idx+1 for 1-indexed row numbers)
            "Frequency": count,
            "Acquiror Macro Industry": row["Acquiror Macro Industry"]
        })

# Convert the results into a DataFrame for display
global_result_df = pd.DataFrame(global_results)

if global_result_df.empty:
    print(f"\nNo rows found with the word '{global_word}' in the 'Deal Synopsis' column.")
else:
    print(f"\nRows where the word '{global_word}' appears in the 'Deal Synopsis' column:")
    print(global_result_df)
  import re
from collections import Counter

# Ensure required columns exist
if "Deal Synopsis" not in evaluation_data.columns:
    raise ValueError("Column 'Deal Synopsis' not found in the dataset.")
if "Acquiror Macro Industry" not in evaluation_data.columns:
    raise ValueError("Column 'Acquiror Macro Industry' not found in the dataset.")

# 1. Take input for Acquiror Macro Industry and filter rows (case-insensitive)
acquiror_input = input("Enter the Acquiror Macro Industry: ").strip().lower()
filtered_data = evaluation_data[
    evaluation_data["Acquiror Macro Industry"].str.lower() == acquiror_input
]

if filtered_data.empty:
    print(f"No rows found for Acquiror Macro Industry: {acquiror_input}")
else:
    print(f"Found {len(filtered_data)} rows for Acquiror Macro Industry: {acquiror_input}\n")

    # 2. Define default stop words and allow user to add more
    stop_words = {"the", "in", "to", "or", "of", "and", "a", "for",
                  "on", "with", "at", "by", "from", "as", "an", "is",
                  "it", "this", "that", "be", "which"}

    additional_stops = input("Enter additional stop words separated by commas (or press Enter to skip): ").strip()
    if additional_stops:
        extra_stop_words = {word.strip().lower() for word in additional_stops.split(',') if word.strip()}
        stop_words = stop_words.union(extra_stop_words)

    # 3. Row-by-row frequency analysis on "Deal Synopsis" (excluding stop words)
    print("Frequency analysis for each row:")
    for idx, row in filtered_data.iterrows():
        text = str(row["Deal Synopsis"])
        # Clean the text: lowercase and remove punctuation
        text_clean = re.sub(r'[^\w\s]', '', text.lower())
        words = text_clean.split()
        # Filter out stop words
        filtered_words = [word for word in words if word not in stop_words]
        freq = Counter(filtered_words)
        print(f"Row {idx} (Acquiror Macro Industry: {row['Acquiror Macro Industry']}): {dict(freq)}")

    # 4. Collective analysis: combine all Deal Synopsis text from the filtered rows
    combined_text = ' '.join(filtered_data['Deal Synopsis'].dropna().tolist())
    combined_text_clean = re.sub(r'[^\w\s]', '', combined_text.lower())
    all_words = combined_text_clean.split()
    # Remove stop words from the combined text
    all_words_filtered = [word for word in all_words if word not in stop_words]
    combined_freq = Counter(all_words_filtered)

    # Ask user for number of most frequent words to display
    top_n = int(input("Enter the number of most frequent words to display: "))

    # Get and display the top N most frequent words in the combined text
    if combined_freq:
        most_common_words = combined_freq.most_common(top_n)
        print(f"\nThe top {top_n} most frequent words in the combined text are:")
        for word, count in most_common_words:
            print(f"'{word}': {count}")
    else:
        print("No words found in the combined text.")

    # 5. Take input of multiple words and display their frequencies in the combined text
    words_input = input("Enter the words to search in the combined text (separated by commas): ")
    target_words = [w.strip().lower() for w in words_input.split(',') if w.strip()]

    print("\nFrequency of the specified words in the combined text:")
    for word in target_words:
        print(f"'{word}': {combined_freq.get(word, 0)}")

