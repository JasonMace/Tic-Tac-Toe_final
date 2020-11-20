string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
count = 0

for char in string:
    for letter in vowels:
        if char == letter:
            count += 1
print(count)
