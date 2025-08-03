def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        import string
        for p in string.punctuation:
            content = content.replace(p, "")
        content = content.lower()

        words = content.split()
        word_count = {}

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        
        print("\n📄 Word Frequencies (sorted):")
        for word in sorted(word_count):
            print(f"{word}: {word_count[word]}")

    except FileNotFoundError:
        print("❌ File not found. Please check the file path.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

def main():
    file_path = input("Enter the path to the text file: ")
    count_words_in_file(file_path)

main()

#Enter the path to the text file: sample.txt

#📄 Word Frequencies (sorted):
#a: 2
#and: 3
#file: 1
#hello: 1
#this: 2
#world: 1
#Hello world! This is a sample file.
#This file is simple and clean. And fun.
