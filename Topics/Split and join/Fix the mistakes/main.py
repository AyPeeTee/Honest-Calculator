text = input()
words = text.split()
string = ""
for word in words:
    if word.lower().startswith("www."):
        print(word)
    elif word.lower().startswith("http://"):
        print(word)
    elif word.lower().startswith("https://"):
        print(word)
