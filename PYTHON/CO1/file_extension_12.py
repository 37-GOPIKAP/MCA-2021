#prgm to print the extension of a file
filename=input("enter the file name:")
file_extn=filename.split(".")
print("the extension of the file is:"+repr(file_extn[-1]))
