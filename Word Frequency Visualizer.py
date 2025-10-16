# Task 1: Word Frequency Visualizer
# Step 1: Input a paragraph from the user
text = input("Enter a paragraph: ")

# Step 2: Clean text - remove punctuation & convert to lowercase
import string
clean_text = text.lower()
for p in string.punctuation:
    clean_text = clean_text.replace(p, "")

# Step 3: Split text into words and count frequency
words = clean_text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Step 4: Sort and display top 5 frequent words
sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print("\nTop 5 most frequent words:")
for word, count in sorted_words[:5]:
    print(f"{word}: {count}")

# BONUS: Bar chart using matplotlib
import matplotlib.pyplot as plt

top_words = dict(sorted_words[:5])
plt.bar(top_words.keys(), top_words.values(), color='skyblue')
plt.title("Top 5 Word Frequencies")
plt.xlabel("Words")
plt.ylabel("Count")
plt.show()
