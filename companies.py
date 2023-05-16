def interchange_and(sentence):
    words = sentence.split()
    i = 0
    while i < len(words) - 1:
        if words[i] == "and":
            # If the current word is "and", swap the previous and next words
            words[i-1], words[i+1] = words[i+1], words[i-1]
            # Increment i by 2 to skip the swapped words
            i += 2
        else:
            # Otherwise, increment i by 1 to move to the next word
            i += 1
    # Join the words back together into a sentence
    return " ".join(words)

# Get input sentence from user
input_sentence = input("Enter a sentence: ")

# Call interchange_and function to get output sentence
output_sentence = interchange_and(input_sentence)

# Print the output sentence
print(output_sentence)
