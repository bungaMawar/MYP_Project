print ('Hello World')
print ('Wassup')
myFile = open('my_file.txt')
print(myFile.read())
myFile.close()
print ('This is legit all I can do right now')
print ("it's real annoying")
test = 'this is a test string'

for letter in test:
    if letter == 'a':
        break
    print (letter)
result = None
while result != 21:
    result = int(input ('What is 9 + 10? '))
    if result == 21:
        print ('Correct!!')
    elif result == 19:
        print("There's another answer to that y'know...")
    else:
        print ('Wrong!!')

