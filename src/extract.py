import nltk
file_path = r"C:\Users\Maha\Downloads\time_machine.txt"

# Read the file
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        book_text = file.read()
except FileNotFoundError:
    print("Error: File not found. Check the file path and try again.")
    exit()

start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK THE TIME MACHINE ***"
start_pos = book_text.find(start_marker) + len(start_marker)
book_text = book_text[start_pos:]

ch1_start = book_text.find("I.\n Introduction\n\n") + len("I.\n Introduction\n\n")
ch2_start = book_text.find("II.")  # start of Chapter II

text=book_text[ch1_start:ch2_start].replace("\n", " ").replace(" "," ").strip()

print(f"Chapter 1 length: {len(text)} characters")
print(f"First 100 characters: {text[:100]}...")