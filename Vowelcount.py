# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):

    vowels = 'aeiou'
    counter = 0
    for char in sentence:
        if char in vowels:
            counter += 1

    return print(counter)
    
    # Different not so efficient approach

    # sent_lst = list(sentence)
    # vowel_count = []
    # vowels = "aeiou"
    # for char in sent_lst:
    #     if char in vowels:
    #         vowel_count.append(char)
    # return len(vowel_count)

get_count("aeiou")