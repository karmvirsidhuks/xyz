vowels = ('a', 'e', 'i', 'o', 'u')
def vowel(char):
    if char in vowels:
        return True
    return False


print(vowel(9))
print(vowel('e'))
print(vowel('b'))