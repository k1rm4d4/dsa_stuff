# imagine a program that when given an input phrase: 
# "There's smart, and there's genius."
# Then given a target phrase: "John Rok was a genuis."

# it must check if this is can be converted to target, and what letters are missing.

#  create letter map of A and B
#  compare A and B, create C (A-B values), non zero is the answer


def get_letter_count(phrase):
    word_count = {}
    for l in phrase:
        if word_count.get(l):
            word_count[l] += 1
        else:
            word_count[l] = 1
    return word_count


def compare_letters(a, b):
    missing = {}
    for letter in b.keys(): 
        if a.get(letter) is None:
            if missing.get(letter):
                missing[letter] += 1
            else: 
                missing[letter] = 1
    return missing



if __name__=="__main__":
    a = "What a lazy fox!"
    b = "Damn that's a wolf!"

    a = get_letter_count(a)
    b = get_letter_count(b)

    print(compare_letters(a, b))

