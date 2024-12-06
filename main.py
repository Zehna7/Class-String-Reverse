class StringReverser:
    def reverse_words(self, text):
        return ' '.join(word[::-1] for word in text.split())

text = input("Enter the text that you want reversed: ")
reverser = StringReverser()
reversed_text = reverser.reverse_words(text)
print("Here is the reversed text:", reversed_text)