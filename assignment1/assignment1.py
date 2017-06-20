#Assignment1
import string
print "--- Python Edureka Assignment 1 ---"

task1String = 'Discover, Learning, with, Edureka'
# Task 1:
# to print the:
# a. Number of lowercase a and o in the following sentence.
# b. Number of uppercase L and N in the following sentence.
def task1():
    print "Performing Task : 1"
    lowercase_ao = 0
    uppercase_LN = 0
    for index in range(0,len(task1String)):
        if ord(task1String[index]) == 97 or ord(task1String[index]) == 111 :
            lowercase_ao += 1
        elif ord(task1String[index]) == 76 or ord(task1String[index]) == 78:
            uppercase_LN += 1
        else:
            pass
    
    print "Number of lowercase a and o: ",lowercase_ao," Number of uppercase L and N: ",uppercase_LN

task2String = 'www.edureka.in'
# Task 2:
# remove the following from:
# www.edureka.in
# a. Remove all w's before and after .edureka.
# b. Remove all lowercase letter before and after .edureka.
# c. Remove all printable characters
def task2():
    print "Performing Task : 2"
    print task2String
    print "After removing all w's before and after .edureka. is: ", task2String.strip('w')
    print "After removing all lowercase letter before and after .edureka.:", task2String.strip(string.lowercase)
    print "After removing all printable characters: ", task2String.strip(string.printable)

task3List = [0X7AE, 3+4j, -01234, 3.14e-2]
# Task 3:
# Identify the type of numbers:
# a. 0X7AE
# b. 3+4j
# c. -01234
# d. 3.14e-2
def task3():
    print "Performing Task : 3"
    for number in task3List:
        numberType = (str(type(number))).split("'")[1]
        print "Number",number,"is of type:",numberType

# Task 4():
# String Formatting Operator % which should include the following conversions:
# a. Character
# b. Signed decimal integer
# c. Octal integer
# d. Hexadecimal integer (UPPERcase letters)
# e. Floating point real number
# f. Exponential notation (with lowercase 'e')
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)
def task4():
    print "Performing Task : 4"
    luckyNumber = 23
    print "For lucky number %d character is: %s"%(luckyNumber, chr(luckyNumber))
    print "For lucky number %d Signed decimal integer is: %d"%(luckyNumber, int(luckyNumber))
    print "For lucky number %d Octal integer is: %s"%(luckyNumber, oct(luckyNumber))
    print "For lucky number %d Hexadecimal integer is: %s"%(luckyNumber, hex(luckyNumber))
    print "For lucky number %d Floating point real number is: %f" % (luckyNumber, float(luckyNumber))
    print "For lucky number %d Exponential notation is: %s" % (luckyNumber, (luckyNumber))

task1()
task2()
task3()
task4()
