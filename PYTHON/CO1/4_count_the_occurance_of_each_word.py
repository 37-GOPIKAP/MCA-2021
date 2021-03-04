text="Python is a popular programming language which is developed by Guido Van Rossum "
for i in text.strip().split():
    print("Number of occurence of word ","\"",i,"\""," is :",text.strip().split().count(i))
