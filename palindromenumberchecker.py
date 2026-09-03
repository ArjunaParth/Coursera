n= input('Enter the number you want to check ')
string1= int (n)
string2 = string1
l= int(len(n))
newstring = 0
for i in range (0,l):
    newstring = (10*newstring) + (string1%10)
    string1=string1//10
if (string2 == newstring):
    print(string2,"is a palindrome number")
else :
    print (string2,"isnt a palindrome number")

    