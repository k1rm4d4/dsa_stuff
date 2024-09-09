


def reverse(word):
    if word == "":
        return ""
    # print(f"{word[-1]} + {word[:len(word) - 1 ]}")
    return word[-1] + reverse(word[:len(word)-1])



print(reverse("apple"))