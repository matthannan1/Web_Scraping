def anti_vowel(text):
  new = ""
  vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
  for a in text:
    if a not in vowels:
      new = new + a
  return new  


phrase = input("What is your phrase? ")
print(anti_vowel(phrase))  