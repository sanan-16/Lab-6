def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    char_freq1 = {}
    char_freq2 = {}

    for char in str1:
        char_freq1[char] = char_freq1.get(char, 0) + 1

    for char in str2:
        char_freq2[char] = char_freq2.get(char, 0) + 1

    return char_freq1 == char_freq2

string1 = "listen"
string2 = "silent"
result = are_anagrams(string1, string2)

if result:
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
