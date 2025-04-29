# Extract all entries from the "Deal Synopsis" column of the dataset
allTexts = evaluation_data['Deal Synopsis'].tolist()
print("Total text entries:", len(allTexts))

# Combine all the texts into a single string for analysis
combinedText = ' '.join(allTexts)
# Extract all text entries from the "Deal Synopsis" column and combine them
allTexts = evaluation_data['Deal Synopsis'].tolist()
combinedText = ' '.join(allTexts)

# Generate a word cloud for the entire Deal Synopsis column
wordcloud_all = WordCloud().generate(combinedText)
plt.imshow(wordcloud_all, interpolation='bilinear')
plt.axis("off")
plt.show()
