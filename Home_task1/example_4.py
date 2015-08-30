"""
Modul for calculation lexem statistic in the texts

"""
import string
my_dict = {}

# determination conditions for word processing in the  string sentence
strip = string.whitespace + string.punctuation + string.digits + "\"'"
# open text file
infile = open("test_f.txt")
# reading a line
for line in infile:
    for word in line.lower().split():
        word = word.strip(strip)
        if len(word) > 2:
            my_dict[word] = my_dict.get(word, 0) + 1
# sorted dictionary per word 
for word in sorted(my_dict):
    print "lex: " + word + "\t" + "N of lex in text " + str(my_dict[word])
print my_dict
