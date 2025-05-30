# Create a text analyzer that:
# 1. Takes a paragraph of text as input
# 2. Splits it into sentences (assume '.' ends sentences)
# 3. For each sentence, count words and characters
# 4. Find the longest and shortest sentences
# 5. Create a list of unique words (case-insensitive)
# 6. Count frequency of each word
# 7. Present results in a formatted report

# Your code here:

text = """Python is amazing. It has simple syntax. 
              Python is used in data science. Machine learning uses Python too."""

text_sentence = text.split(".")
text_sentence.pop()
# print(text_sentence)
# 3. For each sentence, count words and characters
text_len = []
for i, p in enumerate(text_sentence):
    # count words
    p_word = p.strip().split()
    p_word_count = len(p_word)
    p_char_count = len(p.strip())
    text_len.append((i, p_word_count, p_char_count))

# 4. Find the longest and shortest sentences
text_len.sort(key=lambda x: x[2], reverse=True)

longest_sentence_index = text_len[0][0]
shortest_sentence_index = text_len[-1][0]

print(f"Longest sentence: {text_sentence[longest_sentence_index]}")
print(f"Shortest sentence: {text_sentence[shortest_sentence_index]}")

# 5. Create a list of unique words (case-insensitive)
word_count = {}
all_words = []
for sentence in text_sentence:
    words = sentence.strip().split()
    for word in words:
        clean_word = word.lower().strip(".,!?")
        all_words.append(clean_word)

# count quency
for word in all_words:
    word_count[word] = word_count.get(word, 0) + 1

# unique word
unique_word = []
for word in word_count:
    if word_count.get(word, 0) == 1:
        unique_word.append(word)

# unique words
unique_words = list(word_count.keys())
# unique_words2 = []
# unique_words2.append(word_count.keys())
# 7. Present results in a formatted report
print("=" * 60)
print("📝 TEXT ANALYSIS REPORT".center(60))
print("=" * 60)

print(f"\n📊 BASIC STATISTICS:")
print(f"  Total sentences: {len(text_sentence)}")
print(f"  Total unique words: {len(unique_words)}")
print(f"  Total words: {sum(word_count.values())}")

print(f"\n📋 SENTENCE ANALYSIS:")
for i, sentence in enumerate(text_sentence):
    words = sentence.strip().split()
    word_count_sentence = len(words)
    char_count = len(sentence.strip())
    print(
        f"  Sentence {i+1}: {word_count_sentence:2d} words, {char_count:2d} characters"
    )
    print(f'    "{sentence.strip()}"')

print(f"\n🏆 LONGEST SENTENCE:")
print(f'  "{text_sentence[longest_sentence_index].strip()}"')
print(f"  ({text_len[0][1]} words, {text_len[0][2]} characters)")

print(f"\n🏆 SHORTEST SENTENCE:")
print(f'  "{text_sentence[shortest_sentence_index].strip()}"')
print(f"  ({text_len[-1][1]} words, {text_len[-1][2]} characters)")

print(f"\n📝 VOCABULARY ANALYSIS:")
print(f"  Unique words: {unique_words}")

print(f"\n📊 WORD FREQUENCY:")

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words:
    print(f"    '{word}': {count}")

print("=" * 60)
