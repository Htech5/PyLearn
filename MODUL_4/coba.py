def reverse_first_last(text):
    # Split the text into words
    words = text.split()

    # Check if there are at least two words
    if len(words) >= 2:
        # Swap the first and last words
        words[0], words[-1] = words[-1], words[0]
        # Join the words back into a string
        result = " ".join(words)
    else:
        # If there is only one word, just reverse it
        result = text[::-1]

    # Print the result
    print(result)


# Example usage:
input_text = input("Enter a sentence: ")
reverse_first_last(input_text)
