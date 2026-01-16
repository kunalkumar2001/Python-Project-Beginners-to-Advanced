from textblob import TextBlob

text = input("Enter a sentence with potential spelling errors: ")

corrected_text = TextBlob(text).correct()

print("Corrected Sentence:", corrected_text)
