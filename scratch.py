def consec_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if type(string) != str:
        return False
    
    y = 0
    vowel_count = 0

    for x in string:
        if x == vowels[y]:
            vowel_count += 1
            y += 1
            if y == 5:
                y = 0
            continue
    
    return vowel_count