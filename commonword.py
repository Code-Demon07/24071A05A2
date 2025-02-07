#Write a function that finds the most common word in a given text.
import re

def most_common_word(text):
    
    words = re.findall(r'\b\w+\b', text.lower())

    if words:
        most_common = max(set(words), key=words.count)
        return most_common
    return None

text = "This is a test. This test is only a test."
result = most_common_word(text)
if result:
    print(f"The most common word is '{result}'.")
else:
    print("No words found in the text.")
