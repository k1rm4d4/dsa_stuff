
def reverse(word):
    if word == "":
        return ""
    # print(f"{word[-1]} + {word[:len(word) - 1 ]}")
    return word[-1] + reverse(word[:len(word)-1])

def remove_white(sentence):
    return "".join(sentence.split())

def is_pal(s):
    # remove whitespace here
    # print(remove_whitespace(s))
    rev_s = reverse(s)
    if s == rev_s: 
        return True
    return False 


print(is_pal("madam i'm adam"))
print(is_pal("nitin"))
print(is_pal(""))