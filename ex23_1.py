# Solution to the problem "Forgotten Language" from CodeChef.com
# available at: https://www.codechef.com/problems/FRGTNLNG
# Level: Beginer

# This function validates if a string complains with the constraint
# 1 <= length of any string in the input <= 5
def word_len(word):
    valid_word = False
    if (len(word) > 1 and len(word) <= 5):
        valid_word = True
    return valid_word

filename = raw_input()
in_file = open(filename)

num_tests = int(in_file.readline())
# Valitate constain 1 <= num_tests <= 20
if (num_tests >= 1 and num_tests <= 20):
    for test in range(0, num_tests):
        # Read text case information
        test_case = str.split(in_file.readline())
        # Validate constrain 1 <= num_strings <= 100
        num_strings = int(test_case[0])
        if (num_strings >= 1 and num_strings <= 100):
            # Validate constrain 1 <= num_phrases <= 50
            num_phrases = int(test_case[1])
            if (num_phrases >= 1 and num_phrases <= 50):
                # Read the words in the forgotten language
                forgotten_words = str.split(in_file.readline())
                # Create a list to define if a forgotten word has been found
                # in modern language
                forgotten_words_found = []
                for i in range(0, len(forgotten_words)):
                    forgotten_words_found.append("NO")
                # Start reading all the phrases in the modern language
                for phrase in range (0, num_phrases):
                    current_phrase = str.split(in_file.readline())
                    # Validate 1 <= phrase_len <= 50
                    phrase_len = int(current_phrase[0])
                    if (phrase_len >= 1 and phrase_len <=50):
                        # Look for the existense of every forgotten word in
                        # the current phrase
                        for i in range(0, len(forgotten_words)):
                            if (word_len(forgotten_words[i])):
                                for j in range(0, phrase_len):
                                    if (word_len(current_phrase[j])):
                                        # Was the word found before?
                                        if (forgotten_words_found[i] == "NO"):
                                            for k in range(1, phrase_len):
                                                if (word_len(current_phrase[k])):
                                                    if (forgotten_words[i] 
                                                        == current_phrase[k]):
                                                        forgotten_words_found[i] = "YES"
                print ' '.join(forgotten_words_found)