# simple_code.py
# HackBio Stage Zero Project – Team Valine
# A simple Python script to count words in the essay.md file

# Open the essay file and read its content
with open("essay.md", "r", encoding="utf-8") as file:
    text = file.read()

# Count words by splitting text by spaces
word_count = len(text.split())

# Print the result
print(f"Your essay contains {word_count} words.")
