# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    if (sorted(word) == sorted(anagram)):
        print('its true, ' + anagram +' is an anagram of '+ word)
        return True
    else:
        print('its false, ' + anagram +' is not an anagram of '+ word)
        return False

#testing
find_anagrams("hello", "check") 
find_anagrams("below", "elbow") 
