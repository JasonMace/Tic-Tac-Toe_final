cases = ["https://", "http://", "www."]

words = input().split()
for word in words:
    for starter in cases:
        if word.startswith(starter) or word.startswith(starter.upper()):
            print(word)
