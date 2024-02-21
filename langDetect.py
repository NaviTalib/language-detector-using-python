from langdetect import detect

def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "Unknown"

# Get user input
text = input("Enter the text for language detection: ")

# Detect language
language = detect_language(text)
print("Detected language:", language)
