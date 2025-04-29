import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

# Prompt the user to choose the filter type for word cloud analysis
print("Select filter type for word cloud analysis:")
print("1: Row number")
print("2: Acquiror Macro Industry")
print("3: Target Macro Industry")
filter_choice = input("Enter your choice (1, 2, or 3): ").strip()

if filter_choice == "1":
    # Filter by row number
    row_input = input("Enter the row index for generating the word cloud: ").strip()
    try:
        row_index = int(row_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        exit()

    # Check if row index is within bounds
    if row_index < 0 or row_index >= len(evaluation_data):
        print(f"Row index out of bounds. Please enter a value between 0 and {len(evaluation_data)-1}.")
    else:
        # Extract text from the specified row in the "Deal Synopsis" column
        row_text = evaluation_data.iloc[row_index]['Deal Synopsis']
        print(f"Generating word cloud for row {row_index}.")

        # Generate the word cloud for that row
        wordcloud_row = WordCloud().generate(row_text)
        plt.imshow(wordcloud_row, interpolation='bilinear')
        plt.axis("off")
        plt.title(f"Word Cloud for Row {row_index}")
        plt.show()

elif filter_choice == "2":
    # Filter by Acquiror Macro Industry
    acquiror_input = input("Enter the Acquiror Macro Industry: ").strip().lower()
    # Filter the DataFrame for matching Acquiror Macro Industry (case-insensitive)
    filtered_data = evaluation_data[
        evaluation_data["Acquiror Macro Industry"].str.lower() == acquiror_input
    ]
    if filtered_data.empty:
        print(f"No rows found for Acquiror Macro Industry: {acquiror_input}")
    else:
        print(f"Found {len(filtered_data)} rows for Acquiror Macro Industry: {acquiror_input}.")
        # Combine text from all filtered rows in the "Deal Synopsis" column
        combined_text = ' '.join(filtered_data['Deal Synopsis'].dropna().tolist())
        wordcloud_acquiror = WordCloud().generate(combined_text)
        plt.imshow(wordcloud_acquiror, interpolation='bilinear')
        plt.axis("off")
        plt.title(f"Word Cloud for Acquiror Macro Industry: {acquiror_input}")
        plt.show()

elif filter_choice == "3":
    # Filter by Target Macro Industry
    target_input = input("Enter the Target Macro Industry: ").strip().lower()
    # Filter the DataFrame for matching Target Macro Industry (case-insensitive)
    filtered_data = evaluation_data[
        evaluation_data["Target Macro Industry"].str.lower() == target_input
    ]
    if filtered_data.empty:
        print(f"No rows found for Target Macro Industry: {target_input}")
    else:
        print(f"Found {len(filtered_data)} rows for Target Macro Industry: {target_input}.")
        # Combine text from all filtered rows in the "Deal Synopsis" column
        combined_text = ' '.join(filtered_data['Deal Synopsis'].dropna().tolist())
        wordcloud_target = WordCloud().generate(combined_text)
        plt.imshow(wordcloud_target, interpolation='bilinear')
        plt.axis("off")
        plt.title(f"Word Cloud for Target Macro Industry: {target_input}")
        plt.show()

else:
    print("Invalid choice. Please enter 1, 2, or 3.")
