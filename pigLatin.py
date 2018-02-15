def translateWord(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0] in vowels:
        pigLatinWord = word + "way"
        return pigLatinWord
    else:
        if len(word) > 1:
            if word[1] in vowels:
                pigLatinWord = word[1:] + word[0] + "ay"
                return pigLatinWord
            else:
                pigLatinWord = word[2:] + word[0] + word[1] + "ay"
                return pigLatinWord
        else:
            return word



print("Welcome to Kenji and Laine's pig latin app. It will translate any sentence to Pig Latin!")
print("If you would like to quit type 'stop'.")
print("----------------------------------------------------------------------------------------")
while True:
    print("")
    sentence = input("Type in a sentence: ")
    sentence = sentence.lower()
    if sentence.replace(' ', '').isalpha():
        if sentence.lower() == "stop":
            break
        words = sentence.split()
        pigLatinSentence = ""
        for word in words:
            pigLatinSentence = pigLatinSentence + translateWord(word) + " "
        print("Pig Latin: " + pigLatinSentence)
    else:
        print("Please type in only letters.")
