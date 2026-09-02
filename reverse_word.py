# A function that reverses the word
def reversed_word(word):
    lowered_word = word.lower()
    limit = len(lowered_word) - 1
    new_sample = []

    while(limit >= 0):
        new_sample.append(lowered_word[limit])
        limit -= 1
    result = " ".join(new_sample)
    return result

word = input("Enter the desired text: ")
print(reversed_word(word))