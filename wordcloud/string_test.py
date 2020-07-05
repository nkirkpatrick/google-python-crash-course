
def string_test(string):

    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
        
    new_string = " "
    final_string = " "

    string_split = string.split()

    for word in string_split:

        # print(word)

        if word.lower() not in uninteresting_words:
        
            for letter in word:
                if letter.isalpha() or letter in punctuations:
                    valid_word = True
                else:
                    valid_word = False
                    break
            if valid_word == True:
                new_string = new_string + " " + word     

    string_split = new_string.split()

    for word in string_split:
        for letter in word:
            if letter.isalpha():
                final_string += letter.lower()
        final_string += " "

    string_split = final_string.split()

    frequencies = {}

    for word in string_split:
        #print(word)
        if word not in frequencies:
            frequencies[word] = 0
        frequencies[word] += 1

    print(final_string)         
    return frequencies

print(string_test("This is a test345 of For Wordclouds% Alice& wonderland.. wordclouds Alice"))


