#Write a python program that takes 2 inputs from the user. The first input is a string and the second input is a letter. The program should remove all occurences of the letter from the given string and print the output. If the letter is not found in the string and the length of string is greater than 3, then remove the first letter and last letter of the given string and print it. Otherwise print the string as it is. [You can assume that all the input will be in lowercase letter]
#Sample Input 1:
#tanjiro kamado
#a
#Sample output 1:
#tnjiro kmdo
#Sample Input 2:
#eren yeager
#k
#Sample Output 2:
#ren yeage
#Sample Input 3:
#hi
#a
#Sample Output 3:
#hi
var1 = "eren yeager"
var2 = "s"
y = ''
for i in range(len(var1)):
    if var2[0] == var1[i]:
        y = var1.replace(var2[0],'')
    elif var2[0] != var1[i] and len(var1)>3:
        y = var1[1:i]
    else:
        y = var1
print(y)