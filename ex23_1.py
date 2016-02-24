# Solution to the problem "Forgotten Language" from CodeChef.com
# available at: https://www.codechef.com/problems/FRGTNLNG
# Level: Beginer

# This function validates if a string complains with the constraint
# 1 <= length of any string in the input <= 5
def word_len(word):
    valid_word = false
    if (len(word) > 1 & len(word) <= 5):
        valid_word = true
    return valid_word

in_file = open("input1.txt")

num_tests = int(in_file.readline())
# Valitate constain 1 <= num_tests <= 20
if (num_tests >= 1 & num_tests <= 20):
    for test in range(1, num_tests):
        # Read text case information
        test_case = str.split(in_file.readline())
        # Validate constrain 1 <= num_strings <= 100
        num_strings = int(test_case[0])
        if (num_strings >= 1 & num_strings <= 100):
            # Validate constrain 1 <= num_phrases <= 50
            num_phrases = int(test_case[1])
            if (num_phrases >= 1 & num_phrases <= 50):
                # Read the words in the forgotten language
                forgotten_words = str.split(in_file.readline())
                # Start reading all the phrases in the modern language
                for phrase in range (1, num_phrases):
                    current_phrase = str.split(in_file.readline())
                    # Validate 1 <= phrase_len <= 50
                    phrase_len = int(current_phrase[0])
                    if (phrase_len >= 1 & phrase_len <=50):
                        # Validating constrain 1 <= word_len <= 5
                        print "We can validate the case :", test
                    else:
                        print "Phrase %d can't be analyzed: %r" % (phrase,
                        current_phrase)                        
            else:
                print "Invalid number of phrases in the modern language."
        else:
            print "Invalid number of strings in the forgotten language."
else:
    print "Invalid number of test cases."