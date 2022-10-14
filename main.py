print ("***************************************")
print ("****   Starting the bookbot code   ****")
print ("***************************************")

# Open the file where the book text is located
with open("books/frankenstein.txt") as f:
    file_contents = f.read()

# Spliting the complete text into individual words
num_of_words = file_contents.split()
count = 0

# initializing a dictionary to store the number of occurence of each character
char_dict = {}

# Counting the number of words and the occurence of each character in each word
for i in num_of_words:
    i = i.lower()
    count += 1
    # populating the dictionary of the occurence of characters
    for l in list(i):
        if l in char_dict:
            char_dict[l] += 1
        else:
            char_dict[l] = 1

# print("*"*89)
# print(char_dict)
# print("*"*89)

print("---- Begin report of books/frankenstein.txt ----")
print(f'The total of {count} words found in the document')
print("+++++++++++++++++++++++++++++++++++++++++++++++++")

# Looping through the dictionary sorted in reverse order
for i in dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True)):
    if char_dict[i] > 1:
        print (f'The "{i}" character was found {char_dict[i]} times')
    else:
        print (f'The "{i}" character was found {char_dict[i]} time')

print("------ End report books/frankenstein.txt -------")