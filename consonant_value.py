def consonant_value(word):
    max_value = 0
    current_value = 0
    vowels =['a', 'e', 'i', 'o', 'u']

    for letter in word:
        if letter not in vowels:
            current_value += ord(letter) - ord('a') + 1
        else:
            if current_value > max_value:
                max_value = current_value
            current_value = 0
    if current_value > max_value:
        max_value = current_value

    return max_value
        
print(consonant_value("zodiac"))
            
