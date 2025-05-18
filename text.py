import os
import io
import re
from collections import Counter
def chunk(file_path):
    file_size_bytes = os.path.getsize(file_path)
    file_size_kb = file_size_bytes
    print(f"File size: {file_size_kb:.2f} KB")
    z=int(input("enter the number in how many parts your want to divide"))
    #not to upload file
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
    part_size=len(data)//z
    for i in range(z):
        start = i * part_size
        end = (i + 1) * part_size if i < 3 else len(data)
        with open(f"part_{i+1}.text", 'w', encoding='utf-8') as part_file:
            part_file.write(data[start:end])
        print(f"Written part_{i+1}.text")
    print("✅ File has been split into"+str(z)+"equal parts.")
    return z
z=chunk(file_path="C:\Projects2\Scrape\input.text")

combined_text=""
for i in range(1, z + 1):
    with open(f"part_{i}.text", "r", encoding="utf-8") as f:
        combined_text += f.read()
words = re.findall(r'\b\w+\b', combined_text.lower())
word_counts = Counter(words)
most_common = word_counts.most_common(10)

print("\n🔝 Top 10 most frequent words:")
# for word, count in most_common:
#     print(f"{word}: {count} times")

# Print the most frequent one
print(most_common)

most_common_word = most_common[0][0]
most_common_count = most_common[0][1]
print(f"\n🔥 The most frequent word is '{most_common_word}' with {most_common_count} occurrences.")
dict1={}
for word, count in most_common:
    dict1[word]=count
    most_common_word = max(dict1, key=dict1.get)
    most_common_value = dict1[most_common_word]
print(f"The most Frequient word is '{most_common_word}'")
print(f"Total occurrences:'{most_common_value}'")


# Index

# Make sure everything is lowercase for consistency
combined_text_cleaned = combined_text.lower()
search_word = most_common_word.lower()

# Find all starting indexes of the most common word(rf'\b{most_common_word}\b'
matches = [match.start()-1 for match in re.finditer(rf'\b{re.escape(search_word)}\b', combined_text_cleaned)]

if matches:
    print(f"🔍 The word '{most_common_word}' appears at these indexes: {matches}")
    print(f"🔁 Total occurrences: {len(matches)}")
else:
    print(f"❌ The word '{most_common_word}' was not found.")



