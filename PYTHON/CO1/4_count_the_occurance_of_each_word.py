#count the occurance of each word in a line of text
text="Python is a popular programming language which is developed by Guido Van Rossum "
for i in text.split():
    print("Number of occurence of word ","\"",i,"\""," is :",text.split().count(i))
