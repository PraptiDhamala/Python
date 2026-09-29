def word_count(text):
    """Count how often each word appears in a string."""
    counts = {}
    for word in text.lower().split():
        word = word.strip(".,!?")
        counts[word] = counts.get(word, 0) + 1
    return counts


text = "The cat sat on the mat. The dog sat too!"
result = word_count(text)

# Sort by frequency, highest first
top = sorted(result.items(), key=lambda item: item[1], reverse=True)

# List comprehension: words that appear more than once
repeated = [word for word, n in result.items() if n > 1]

print(top[:3])    # [('the', 3), ('sat', 2), ('cat', 1)]
print(repeated)   # ['the', 'sat']