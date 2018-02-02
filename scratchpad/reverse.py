def reverse(text):
    rev = ""
    for a in text:
        rev = a + rev
    return rev


word = input("What word? ")
print(reverse(word))
