import os
import collections
import re

# Directory containing text files
TEXT_FILES_DIR = "/home/data"

def count_words_in_file(file_path, handle_contractions=False):
    """Reads a file, counts total words, and finds the most common ones."""
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()

    # Handle contractions by splitting them into individual words if needed
    if handle_contractions:
        text = text.replace("'", " ")  # Convert contractions like "I'm" → "I m"

    words = re.findall(r"\b[a-zA-Z]+\b", text)  # Extract only words

    total_words = len(words)
    word_counts = collections.Counter(words)
    top_words = word_counts.most_common(3)  # Get the top 3 words

    return total_words, top_words

def main():
    """Main function to process text files and display results."""
    if not os.path.exists(TEXT_FILES_DIR):
        print(f"Directory '{TEXT_FILES_DIR}' not found!")
        return

    total_word_counts = {}

    print("\na. Total number of words in each text file located at /home/data:")
    for filename in sorted(os.listdir(TEXT_FILES_DIR)):  # Ensure consistent file order
        if filename.endswith(".txt"):
            file_path = os.path.join(TEXT_FILES_DIR, filename)

            # Handle contractions only for "AlwaysRememberUsThisWay-1.txt"
            handle_contractions = filename == "AlwaysRememberUsThisWay-1.txt"

            total_words, top_words = count_words_in_file(file_path, handle_contractions)
            total_word_counts[filename] = total_words

            print(f"  {filename}: {total_words} words")

    # Compute grand total
    grand_total = sum(total_word_counts.values())
    print("\nb. Calculate the grand total of words across both files:")
    print(f"  Grand Total: {grand_total} words")

    # Display top 3 words for IF-1.txt
    file_path = os.path.join(TEXT_FILES_DIR, "IF-1.txt")
    _, top_words = count_words_in_file(file_path)
    print("\nc. Identify the top 3 most frequent words and their respective counts in IF-1.txt:")
    for word, count in top_words:
        print(f"   '{word}': {count} times")

    # Display top 3 words for AlwaysRememberUsThisWay-1.txt with contractions handled
    file_path = os.path.join(TEXT_FILES_DIR, "AlwaysRememberUsThisWay-1.txt")
    _, top_words = count_words_in_file(file_path, handle_contractions=True)
    print("\n\nd. Handle contractions (Examples: I'm, can't, don't) by splitting them into individual words:")
    print("   Top 3 Words in AlwaysRememberUsThisWay-1.txt (with contractions treated as separate words):")
    for word, count in top_words:
        print(f"   '{word}': {count} times")

    # Get and display container IP address
    container_ip = os.popen("hostname -I").read().strip()
    print("\n\ne. Determine the IP address of the machine running the container:")
    print(f"   IP Address: {container_ip}")

if __name__ == "__main__":
    main()
