
if 'evaluation_data' not in globals():
    try:
        evaluation_data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/train.csv')
    except FileNotFoundError:
        print("File '/content/drive/MyDrive/Colab Notebooks/train.csv' not found. Please check the file path or ensure the DataFrame is loaded.")
        exit()

# Prompt the user for the row index for generating the word cloud
row_input = input("Enter the row index for generating the word cloud: ")
try:
    row_index = int(row_input)
except ValueError:
    print("Invalid input. Please enter a valid integer for the row index.")
    exit()

# Check if the row index is within bounds
if row_index < 0 or row_index >= len(evaluation_data):
    print(f"Row index out of bounds. Please enter a value between 0 and {len(evaluation_data)-1}.")
    exit()

# Prompt the user for the column (name or index)
# Valid columns might be "Deal Synopsis", "Acquiror Macro Industry", "Target Macro Industry", etc.
col_input = input("Enter the column name or index from which you want to generate the word cloud (e.g., 'Deal Synopsis'): ")

# Determine if the input is a number (i.e., a column index) or a column name
try:
    col_index = int(col_input)
    # Validate the column index
    if col_index < 0 or col_index >= len(evaluation_data.columns):
        print(f"Column index out of bounds. Please enter a value between 0 and {len(evaluation_data.columns)-1}.")
        exit()
    # Retrieve the actual column name using the index
    column_name = evaluation_data.columns[col_index]
except ValueError:
    # Input is not an integer, so treat it as a column name
    column_name = col_input

# Verify that the column exists in the dataset
if column_name not in evaluation_data.columns:
    print(f"Column '{column_name}' does not exist in the dataset.")
    exit()

# Extract the cell content from the specified row and column
cell_text = evaluation_data.iloc[row_index][column_name]

# Convert the cell to a string if necessary
if not isinstance(cell_text, str):
    cell_text = str(cell_text)

# Check if the cell contains any text
if cell_text.strip() == "":
    print(f"The selected cell at row {row_index} and column '{column_name}' is empty.")
    exit()

# Generate the word cloud for the extracted text
wordcloud_cell = WordCloud().generate(cell_text)

# Plot the word cloud
plt.imshow(wordcloud_cell, interpolation='bilinear')
plt.axis("off")
plt.title(f"Word Cloud for Row {row_index}, Column '{column_name}'")
plt.show()
